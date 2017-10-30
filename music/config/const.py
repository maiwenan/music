#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Constants(object):
	conf_dir = os.path.join(os.path.expanduser('~'), '.musicbox')
	log_path = os.path.join(conf_dir, 'musicbox.log')
	db_config = {
    	"username": "root",
    	"password": "123456",
    	"host": "localhost",
    	"port": "3306",
    	"db_name": "music"
    }


