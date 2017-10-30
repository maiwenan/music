#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
from music.models.db import session, User

def batch_save_users(users):
	add_list = []
	update_list = []
	ids = []

	for user in users:
		if user['userId'] in ids:
			continue
		ids.append(user['userId'])
		user['id'] = user['userId']
		user.pop('userId')
		if 'locationInfo' in user:
			user.pop('locationInfo')
		if 'avatarImgIdStr' in user:
			user.pop('avatarImgIdStr')
		if 'avatarImgId_str' in user:
			user.pop('avatarImgId_str')
		if 'backgroundImgIdStr' in user:
			user.pop('backgroundImgIdStr')
		if 'experts' in user and user['experts'] != None:
			user['experts'] = json.dumps(user['experts'])
		if 'expertTags' in user and isinstance(user['expertTags'], list):
			user['expertTags'] = ','.join(user['expertTags'])
		if 'birthday' in user:
			t = abs(user['birthday'] / 1000)
			user['birthday'] = datetime.fromtimestamp(t)

		if get_by_id(user['id']) == None:
			add_list.append(User(**user))
		else:
			update_list.append(User(**user))

	session.add_all(add_list)
	session.commit()

	return len(add_list)

def get_by_id(id):
	query = session.query(User).filter(User.id == id)
	return query.first()