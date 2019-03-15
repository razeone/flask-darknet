# -*- coding: utf-8 -*-

import os

DEBUG = False
HOME_PATH = os.environ['HOME']
DARKNET_HOME = os.environ['DARKNET_HOME']
WEIGHTS_FILE = os.environ['WEIGHTS_FILE']
CONFIG_FILE = os.environ['CONFIG_FILE']
META_FILE = os.environ['META_FILE']
UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER']
ALLOWED_EXTENSIONS = tuple(['jpg', 'jpeg', 'png'])

# SECRET_KEY = 'testkey'
# DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'flask-website.db')
# DATABASE_CONNECT_OPTIONS = {}

del os
