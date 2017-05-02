#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from utils.exception import *
from model import PublisherModel
from handler.base.base_handler import BaseHandler


class AddHandler(BaseHandler):
    """ 添加发布方 """

    def post(self):
        name = self.get_json_argument('name')
        brief_introduction = self.get_json_argument('brief_introduction')
        logo = self.get_json_argument('logo')
        address = self.get_json_argument('address')

        publisher = self.model_config.first(PublisherModel, name=name)  # TODO: 发布方是否允许重名？
        if publisher:
            raise ServerError(ServerError.USER_EXIST)

        publisher = PublisherModel()
        publisher.name = name
        publisher.brief_introduction = brief_introduction
        publisher.logo = logo
        publisher.address = address
        publisher.is_del = '0'
        publisher.create_time = datetime.datetime.now()
        publisher.update_time = datetime.datetime.now()
        self.model_config.add(publisher)
        return ''
