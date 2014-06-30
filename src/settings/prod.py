# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''

from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'wanding',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

#MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../..', 'media').replace('\\','/'),
MEDIA_ROOT = '/var/data/wanding/media/'
MEDIA_URL = 'http://www.wandingke.com/media/'
FORUM_URL = 'http://bbs.wandingke.com/'
