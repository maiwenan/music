#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
from .base import Base
from .playlist import Playlist
from .song import Song
from .comment import Comment
from .user import User
from music.config.const import Constants

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

_db_config = Constants.db_config
_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(
	_db_config['username'],
	_db_config['password'],
	_db_config['host'],
	_db_config['port'],
	_db_config['db_name'])

engine = create_engine(_url)

# 如果表不存在，则创建表
Base.metadata.create_all(engine)

# 创建Session类型:
Session = sessionmaker(bind=engine)

# 创建session对象:
session = Session()
