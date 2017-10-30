#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	music
"""

from flask import Flask
from .routes.route import init_routes

def create_app(config = None):
	app = Flask('music')

	app.config.update(dict())

	return app

app = create_app()
init_routes(app)



