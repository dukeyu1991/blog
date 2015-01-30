# -*- coding: utf-8 -*-

from tornado.options import define
from tornado.options import options

__default_settings = {
    'app_path': 8300,
    'db_path': 'mysql+mysqldb://scott:yuyiduo@localhost/shengjian',
    'cookie_secret': 'dpKNm@P6-+B3vSY&jcOizoFHZ#MB1F*TyZG0Dd^&',
}


def load_default_options():
    for setting_key, setting_val in __default_settings.iteritems():
        define(setting_key, setting_val)
