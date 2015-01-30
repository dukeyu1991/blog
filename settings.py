# -*- coding: utf-8 -*-

from tornado.options import define

__default_settings = {
    'app_port': 8300,
    'db_path': 'mysql+mysqldb://root:projectdb@localhost/shengjian',
    'cookie_secret': 'dpKNm@P6-+B3vSY&jcOizoFHZ#MB1F*TyZG0Dd^&',
}


def load_default_options():
    for setting_key, setting_val in __default_settings.iteritems():
        define(setting_key, setting_val)
