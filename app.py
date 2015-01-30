# -*- coding: utf-8 -*-

import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from settings import load_default_options
from controllers.handlers import handlers
from tornado.options import options
from tornado.options import define
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


# Options
define('app_path', os.path.dirname(os.path.abspath(__file__)))

load_default_options()  # 加载默认自定义配置


class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            'template_path': os.path.join(options.app_path, 'templates'),
            'static_path': os.path.join(options.app_path, 'static'),
            'xsrf_cookies': True,
            'cookie_secret': options.cookie_secret,
            'login_url': '/login',
            'ui_modules': {},
            'debug': True,
        }
        super(Application, self).__init__(handlers, **settings)
        # tornado.web.Application.__init__(self, handlers, **settings)

        engine = create_engine(options.db_path, convert_unicode=True)

        self.db = scoped_session(sessionmaker(bind=engine))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.app_port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
