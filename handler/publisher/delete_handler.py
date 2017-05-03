#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from utils.exception import *
from model import PublisherModel

from handler.base.base_handler import BaseHandler,handler


class DeleteHandler(BaseHandler):
    """ 删除发布方 """

    @handler
    def post(self):
        publisher_id = self.get_json_argument('publisher_id')
        publisher = self.model_config.first(PublisherModel, id= publisher_id)
        if not publisher:
            raise ServerError(ServerError.PUBLISHER_NOT_EXIST, args=publisher_id)

        publisher.is_del = True
        publisher.update_time = datetime.datetime.now()
        self.model_config.commit()
        return ''
