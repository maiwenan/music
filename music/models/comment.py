#!/usr/bin/env python
# -*- coding: utf-8 -*-

'song model'

from sqlalchemy import Column, Integer, DateTime, Boolean, Text, Float
from .base import Base

class Comment(Base):
	# 表的名字:
	__tablename__ = 'comments'

	# 表的结构:
	id = Column(Integer, primary_key = True)
	beReplied = Column(Text)
	content = Column(Text)
	liked = Column(Boolean)
	likedCount = Column(Integer)
	time = Column(DateTime)
	userId = Column(Integer)
	songId = Column(Integer)
	hasRecommend = Column(Boolean)
	sentiments = Column(Float)
	