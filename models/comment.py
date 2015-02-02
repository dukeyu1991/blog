# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from . import BaseModel


class Comment(BaseModel):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    comment = Column(Text)
    deleted = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey('comment.id'))
