#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gugulethu Ntombela'
SITENAME = "Gugulethu's logs"
SITESUBTITLE = 'thinking & breathing in code'
#SITEURL = 'http://ntombela.vom/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('Scott Hanselman', 'http://hanselman.com/blog')
          )

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/gugulethun'),
          ('github', 'http://github.com/ntombela'),
          ('bitbucket', 'http://bitbucket.org/ntombela'),
          ('gittip', 'http://gittip.com/gugulethun'),
          ('google-plus', 'http://bitbucket.org/gugulethun'),
          ('linkedin', 'http://linkedin.com/gugulethun'),
          ('stackoverflow', 'http://stackoverflow.com/gugulethun')
          )

DISPLAY_PAGES_ON_MENU = True

GITHUB_URL = 'http://github.com/ntombela/'
DISQUS_SITENAME = "ntombela-blog"
TWITTER_USERNAME = 'gugulethun'
DEFAULT_PAGINATION = 10
GOOGLE_ANALYTICS = 'UA-2114039-16'

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
