#!/usr/bin/env python
# -*- coding: utf-8 -*-

'song model'

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, BigInteger
from .base import Base

class Song(Base):
	# 表的名字:
	__tablename__ = 'songs'

	# 表的结构:
	id = Column(Integer, primary_key = True)
	album = Column(Integer)
	audition = Column(Integer)
	commentThreadId = Column(String(20))
	copyFrom = Column(String(255))
	copyright = Column(Integer)
	copyrightId = Column(Integer)
	crbt = Column(String(50))
	dayPlays = Column(Integer)
	disc = Column(String(20))
	duration = Column(Integer)
	fee = Column(Integer)
	ftype = Column(Integer)
	hearTime = Column(Integer)
	mp3Url = Column(String(255))
	mvid = Column(Integer)
	name = Column(String(255))
	no = Column(Integer)
	playedNum = Column(Integer)
	popularity = Column(Integer)
	position = Column(Integer)
	ringtone = Column(String(255))
	rtUrl = Column(String(255))
	rtype = Column(Integer)
	rurl = Column(String(255))
	score = Column(Integer)
	starred = Column(Boolean)
	starredNum = Column(Integer)
	status = Column(Integer),
	transNames = Column(String(255))
