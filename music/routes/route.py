#!/usr/bin/env python
# -*- coding: utf-8 -*-

from music.service.song import get_recommend_comment
from music.service.comment import comment_sentiments

def init_routes(app):
	@app.route('/api/recommend/hotcomment')
	def hot_comment():
		result = get_recommend_comment()
		return result

	@app.route('/api/comment/sentiments')
	def sentiments():
		count = comment_sentiments()
		return str(count)