#!/usr/bin/env python
# -*- coding: utf-8 -*-

'song model'

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, BigInteger
from .base import Base

class User(Base):
	# 表的名字:
	__tablename__ = 'users'

	# 表的结构:
	id = Column(Integer, primary_key = True)
	accountStatus = Column(Integer)
	authStatus = Column(Integer)
	authority = Column(Integer)
	avatarImgId = Column(BigInteger)
	avatarUrl = Column(String(255))
	backgroundImgId = Column(BigInteger)
	backgroundUrl = Column(String(255))
	birthday = Column(DateTime)
	city = Column(Integer)
	defaultAvatar = Column(Boolean)
	description = Column(String(255))
	detailDescription = Column(Text)
	djStatus = Column(Integer)
	expertTags = Column(String(255))
	experts = Column(String(255))
	followed = Column(Boolean)
	gender = Column(Integer)
	mutual = Column(Boolean)
	nickname = Column(String(50))
	province = Column(Integer)
	remarkName = Column(String(50))
	signature = Column(String(255))
	userType = Column(Integer)
	vipType = Column(Integer)
