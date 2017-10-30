#!/usr/bin/env python
# -*- coding: utf-8 -*-

'playlist model'

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, BigInteger
from .base import Base

class Playlist(Base):
    # 表的名字:
	__tablename__ = 'playlists'

	# 表的结构:
	id = Column(Integer, primary_key = True)
	adType = Column(Integer)
	anonimous = Column(Boolean)
	cloudTrackCount = Column(Integer)
	commentCount = Column(Integer)
	commentThreadId = Column(String(20))
	coverImgId = Column(BigInteger)
	coverImgUrl = Column(String(255))
	createTime = Column(DateTime)
	description = Column(Text)
	highQuality = Column(Boolean)
	name = Column(String(50))
	newImported = Column(Boolean)
	ordered = Column(Boolean)
	playCount = Column(Integer)
	privacy = Column(Integer)
	shareCount = Column(Integer)
	specialType = Column(Integer)
	status = Column(Integer)
	subscribed = Column(Boolean)
	subscribedCount = Column(Integer)
	tags = Column(String(255))
	totalDuration = Column(Integer)
	trackCount = Column(Integer)
	trackNumberUpdateTime = Column(DateTime)
	trackUpdateTime = Column(DateTime)
	updateTime = Column(DateTime)
	userId = Column(Integer)

