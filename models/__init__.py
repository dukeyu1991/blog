# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

from models.user import User
from models.article import Article
from models.comment import Comment


def init_db(engine):
    BaseModel.metadata.create_all(engine)
