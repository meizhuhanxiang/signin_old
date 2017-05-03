#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from utils.exception import *
from model import PublisherModel
from handler.base.base_handler import BaseHandler, handler


class ModifyHandler(BaseHandler):
    """ 修改发布方 """

    @handler
    def post(self):
        publisher_id = self.get_json_argument('publisher_id')
        name = self.get_json_argument('name')
        brief_introduction = self.get_json_argument('brief_introduction')
        logo = self.get_json_argument('logo')
        address = self.get_json_argument('address')

        publisher = self.model_config.first(PublisherModel, id= publisher_id)
        if not publisher:
            raise ServerError(ServerError.PUBLISHER_NOT_EXIST, args=publisher_id)

        if not [publisher.name, publisher.brief_introduction, publisher.logo, publisher.address] == \
            [name, brief_introduction, logo, address]:
            publisher.name = name
            publisher.brief_introduction = brief_introduction
            publisher.logo = logo
            publisher.address = address
            publisher.update_time = datetime.datetime.now()
            self.model_config.commit()
        return ''
