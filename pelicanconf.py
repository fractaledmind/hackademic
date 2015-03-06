#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# === BASIC SETTINGS ===
AUTHOR = 'Stephen Margheim'
SITENAME = 'hackademic'
TAGLINE = 'hacking your education'
SITEURL = 'http://smargh.github.io/hackademic/'
DEFAULT_DATE_FORMAT = '%d-%m-%Y'
TIMEZONE = 'America/New_York'
LOCALE = ['en_US']
DEFAULT_LANG = 'en'
THEME = 'themes/pelican-bootstrap3'
THEME_STATIC_DIR = 'theme'

# === CONTENT SETTINGS ===
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['img', 'static']
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'misc'
OUTPUT_PATH = 'output'

# === URL SETTINGS ===
ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}/'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'

EXTRA_PATH_METADATA = {
    'files/github/CNAME': {'path': 'CNAME'},
    'files/github/404.html': {'path': '404.html'},
    'files/github/README.md': {'path': 'README.md'},
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
}

DEFAULT_METADATA = (
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget.
SOCIAL = (
    ('Github', 'http://github.com/smargh'),
    ('Twitter', 'http://twitter.com/s_margheim'),
    ('RSS', 'http://feeds.feedburner.com/smargh'),
)

MENUITEMS = (
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
