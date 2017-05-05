#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from utils.exception import *
from model import ActivityModel
from handler.base.base_handler import BaseHandler, handler


class ModifyHandler(BaseHandler):
    """ 修改活动 """

    @handler
    def post(self):
        activity_id = self.get_json_argument('activity_id')
        admin_id = self.get_json_argument('admin_id')
        time = self.get_json_argument('time')
        content = self.get_json_argument('content')
        place = self.get_json_argument('place')

        activity = self.model_config.first(ActivityModel, id= activity_id)
        if not activity:
            raise ServerError(ServerError.NOT_EXIST, args=activity_id)

        if not [activity.admin_id, activity.time, activity.content, activity.place] == \
            [admin_id, time, content, place]:
            activity.admin_id = admin_id
            activity.time = time
            activity.content = content
            activity.place = place
            activity.update_time = datetime.datetime.now()
            self.model_config.commit()
        return ''
