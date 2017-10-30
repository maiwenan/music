#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
from sqlalchemy import and_
from snownlp import SnowNLP
from music.utils.api import ne
from music.models.db import session, Comment
from music.utils.json import new_alchemy_encoder
import music.service.user as userService

def spider_comments(song_id, offset = 0, limit = 10):
	result = ne.song_comments(song_id, offset, limit)
	if 'hotComments' in result:
		hot_comments = result['hotComments']
		batch_save_comments(hot_comments, song_id)

	return True

def batch_save_comments(comments, song_id):
	add_list = []
	update_list = []
	users = []

	for comment in comments:
		comment['id'] = comment['commentId']
		comment.pop('commentId')
		comment['userId'] = comment['user']['userId']
		users.append(comment['user'])
		comment.pop('user')
		comment['songId'] = song_id
		# 计算 sentiments 得分
		s = SnowNLP(comment.content)
		comment['sentiments'] = s.sentiments

		if len(comment['beReplied']) > 0:
			reply = comment['beReplied'][0]
			user = reply['user']
			data = {
				'content': reply['content'],
				'userId': user['userId'],
				'avatarUrl': user['avatarUrl'],
				'nickname': user['nickname']
			}
			comment['beReplied'] = json.dumps(data)
		else:
			comment['beReplied'] = None

		t = comment['time'] / 1000
		comment['time'] = datetime.fromtimestamp(t)

		if get_by_id(comment['id']) == None:
			add_list.append(Comment(**comment))
		else:
			update_list.append(Comment(**comment))

	# 保存热评信息
	session.add_all(add_list)
	session.commit()

	# 保存用户信息
	userService.batch_save_users(users)

	return len(add_list)

def get_by_id(id):
	query = session.query(Comment).filter(Comment.id == id)
	return query.first()

def get_by_song(song_id):
	query = session.query(Comment).filter(Comment.songId == song_id)
	
	return query.all()

# 获取消极评论
def get_neg_comment(song_id):
	query = session.query(Comment).filter(
		and_(Comment.songId == song_id, Comment.sentiments <= 0.5)
	)

	return query.all()

# 获取积极评论
def get_pos_comment(song_id):
	query = session.query(Comment).filter(
		and_(Comment.songId == song_id, Comment.sentiments > 0.5)
	)

	return query.all()

def comment_sentiments():
	query = session.query(Comment)
	comments = query.all()
	count = 0

	for comment in comments:
		s = SnowNLP(comment.content)
		comment.sentiments = s.sentiments
		count += 1
		session.commit()
	return count


