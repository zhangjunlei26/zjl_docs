#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'zhangjunlei26@gmail.com'
#SITENAME = u'\u4e00\u82b1\u4e00\u4e16\u754c'
SITENAME = u'一叶一世界'
SITEURL = '/'
#https://disqus.com/home/
#添加评论 disqus.com/zhangjunlei26/K#
DISQUS_SITENAME = "zhangjunlei26"
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'en'
USE_FOLDER_AS_CATEGORY = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


PATH = 'content'
OUTPUT_PATH = 'output/'
#拷贝静态目
STATIC_PATHS = ['images']
STATIC_EXCLUDES = []

#插件
PLUGIN_PATHS = []
PLUGINS = []


#拷贝静态文件

#显示页码
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DELETE_OUTPUT_DIRECTORY = False
DEFAULT_PAGINATION = 10

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('weibo', '#'),
          ('facebook', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
