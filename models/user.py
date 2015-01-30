# -*- coding: utf-8 -*-


from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from . import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    phone = Column(String(11), nullable=False)
    password = Column(String(20), nullable=False)

    def __init__(self, name, phone, password):
        self.name = name
        self.phone = phone
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.name, self.fullname)

