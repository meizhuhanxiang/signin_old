#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from utils.exception import *
from model import ActivityModel

from handler.base.base_handler import BaseHandler,handler


class DeleteHandler(BaseHandler):
    """ 删除活动 """

    @handler
    def post(self):
        activity_id = self.get_json_argument('activity_id')
        activity = self.model_config.first(ActivityModel, id=activity_id)
        if not activity:
            raise ServerError(ServerError.NOT_EXIST, args=activity_id)

        activity.is_del = True
        activity.update_time = datetime.datetime.now()
        self.model_config.commit()
        return ''
