#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import TypeDecorator
from sqlalchemy import types
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import BOOLEAN
from sqlalchemy import text
from sqlalchemy import DateTime
from model.base import *

__author__ = 'guoguangchuan'


class ActivityModel(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, nullable=False)
    time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), doc="活动时间")
    content = Column(String(30), nullable=False, server_default=text("''"), doc="活动内容")
    place = Column(String(30), nullable=False, server_default=text("''"), doc="活动地址")
    is_del = Column(BOOLEAN, nullable=False, server_default='0', doc="逻辑删除, true(删除)|false(未删除)")
    update_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    create_time = Column(TIMESTAMP, nullable=False, server_onupdate=text("CURRENT_TIMESTAMP"))
