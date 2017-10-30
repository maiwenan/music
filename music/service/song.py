#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
import random
from music.utils.json import new_alchemy_encoder
from music.utils.api import ne
from music.models.db import session, Song
import music.service.comment as commentService

def batch_save_songs(songs):
	add_list = []
	update_list = []

	for song in songs:
		song.pop('alias')
		song.pop('artists')
		song.pop('bMusic')
		song.pop('hMusic')
		song.pop('lMusic')
		song.pop('mMusic')
		song.pop('rtUrls')
		if len(song['album']) != 0:
			song['album'] = song['album']['id']
		if 'transNames' in song:
			song['transNames'] = ','.join(song['transNames'])
		if get_by_id(song['id']) == None:
			add_list.append(Song(**song))
		else:
			update_list.append(Song(**song))

	session.add_all(add_list)
	session.commit()

	# 获取歌曲的热评
	for song in add_list:
		commentService.spider_comments(song.id)

	return len(add_list)

def get_by_id(id):
	query = session.query(Song).filter(Song.id == id)
	return query.first()

# 获取随机热评评论，并根据status值判断是否是获取积极或者消极类型的评论
def get_recommend_comment(status = None):
	query = session.query(Song)
	count = query.count()
	result = []

	while len(result) < 10:
		num = random.randint(0, count) - 1
		song = query[num]
		if status == 'positive':
			comments =  commentService.get_pos_comment(song.id)
		elif status == 'negative':
			comments =  commentService.get_neg_comment(song.id)
		else:
			comments = commentService.get_by_song(song.id)
		if len(comments) > 0:
			result.append({
				"song": song,
				"comment": comments[random.randint(0, len(comments) - 1)]
			})

	return json.dumps(result, cls = new_alchemy_encoder(), check_circular = False)

