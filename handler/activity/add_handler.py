#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from model import ActivityModel
from handler.base.base_handler import BaseHandler, handler


class AddHandler(BaseHandler):
    """ 添加活动 """

    @handler
    def post(self):
        current_time = datetime.datetime.now()
        admin_id = self.get_json_argument('admin_id')
        time = self.get_json_argument('time')
        content = self.get_json_argument('content')
        place = self.get_json_argument('place')

        # activity = self.model_config.first(ActivityModel)  # TODO: 根据什么判断是否重复创建了活动？
        activity = ActivityModel(admin_id=admin_id, time=time, content=content, place=place, is_del=False,
                                 create_time=current_time, update_time=current_time)
        self.model_config.add(activity)
        return {'activity_id': activity.id}
