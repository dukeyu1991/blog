# -*- coding: utf-8 -*-

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    @property
    def current_user(self):
        user_id = self.get_secure_cookie('website_user')
        if not user_id:
            return None

        return self.db.get('SELECT * FROM user where id = %s', int(user_id))
