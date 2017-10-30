#!/usr/bin/env python
# -*- coding: utf-8 -*-

'entry'

from .app import app

# from flask import Flask

# app = Flask(__name__)

# print(app)

# @app.route('/')
# def hello_world():
# 	return 'Hello world!'

# from models.db import session, User

# session.add(User(id = 1, signature = '10月歌单烹饪中，快来爱我 ʕ •ᴥ•ʔ ❤️❤️❤️百大10月21号公布，凌晨2点直播哦有没有看的？支持国人电音，欢迎各位国内原创电子制作人自荐作品，投稿或其他合作相关请私信联系哦'))
# session.commit()

# import service.playlist as playlistService

# playlistService.spider_playlists(offset = 0)

# from datetime import datetime

# t = 1508386763278 / 1000
# print(datetime.fromtimestamp(t))


# 创建新User对象:
# new_user = Playlist(id = 5, name = '文安', fullName = '麦文安')
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()