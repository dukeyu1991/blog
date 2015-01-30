# -*- coding: utf-8 -*-

from .. import BaseHandler


class DemoHandler(BaseHandler):
    def get(self):
        return self.render('base.html')