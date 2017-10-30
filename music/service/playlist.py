#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from utils.api import ne
from music.models.db import session, Playlist
import music.service.song as songService
import music.service.user as userService

def spider_playlists(offset = 0, order = 'hot', cat = '全部', limit = 35):
	result = ne.playlists(order, cat, limit, offset)
	playlists = result['playlists']
	total = result['total']
	more = result['more']
	add_list = []
	update_list = []
	users = []

	for playlist in playlists:
		users.append(playlist['creator'])
		playlist.pop('creator')
		playlist.pop('subscribers')
		playlist.pop('tracks')
		if 'coverImgId_str' in playlist:
			playlist.pop('coverImgId_str')
		playlist['tags'] = ','.join(playlist['tags'])
		t = playlist['createTime'] / 1000
		playlist['createTime'] = datetime.fromtimestamp(t)
		t = playlist['trackNumberUpdateTime'] / 1000
		playlist['trackNumberUpdateTime'] = datetime.fromtimestamp(t)
		t = playlist['trackUpdateTime'] / 1000
		playlist['trackUpdateTime'] = datetime.fromtimestamp(t)
		t = playlist['updateTime'] / 1000
		playlist['updateTime'] = datetime.fromtimestamp(t)

		if get_by_id(playlist['id']) == None:
			add_list.append(Playlist(**playlist))
		else:
			playlist['adType'] = 1
			update_list.append(Playlist(**playlist))

	# 保存歌单信息
	session.add_all(add_list)
	# session.bulk_save_objects(update_list)
	session.commit()

	# 保存用户信息
	userService.batch_save_users(users)

	# 获取歌单详情，以便获取歌曲信息
	for playlist in playlists:
		spider_playlist_detail(playlist['id'])
	return more


def spider_playlist_detail(id):
	result = ne.playlist_detail(id)
	track_list = result['tracks']
	songService.batch_save_songs(track_list);
	return True

def get_by_id(id):
	query = session.query(Playlist).filter(Playlist.id == id)
	return query.first()


