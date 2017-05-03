#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from utils.exception import *
from model import PublisherModel
from handler.base.base_handler import BaseHandler, handler


class AddHandler(BaseHandler):
    """ 添加发布方 """

    @handler
    def post(self):
        current_time = datetime.datetime.now()
        name = self.get_json_argument('name')
        brief_introduction = self.get_json_argument('brief_introduction')
        logo = self.get_json_argument('logo')
        address = self.get_json_argument('address')

        publisher = self.model_config.first(PublisherModel, name=name)  # TODO: 发布方是否允许重名？
        if publisher:
            raise ServerError(ServerError.USER_EXIST, args=name)

        publisher = PublisherModel(name=name, brief_introduction=brief_introduction, logo=logo, address=address,
                                   is_del='0', create_time=current_time, update_time=current_time)
        self.model_config.add(publisher)
        return {'publisher_id': publisher.id}
