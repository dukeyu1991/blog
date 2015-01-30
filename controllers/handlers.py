# -*- coding: utf-8 -*-

from tornado.web import url
import login

handlers = [
    url(r'/demo', login.DemoHandler, name='demo')
]
