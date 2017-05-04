#!/usr/bin/python
# -*- coding: utf-8 -*-

from model import ActivityModel
from handler.base.base_handler import BaseHandler, handler


class GetHandler(BaseHandler):
    """ 获取活动信息 """
    @handler
    def post(self):
        activity_ids = self.get_json_argument('activity_ids')
        if activity_ids:
            activities = self.model_config.filter_all(ActivityModel,
                                                      filters=ActivityModel.id.in_(tuple(activity_ids)))
        else:
            activities = self.model_config.all(ActivityModel)

        return [{
            'activity_id': activity.id,
            'admin_id': activity.admin_id,
            'content': activity.content,
            'place': activity.place,
            'time': activity.time,
            'create_time': activity.create_time,
            'update_time': activity.update_time,
            'qr_code': ''  # TODO: 如何获取活动的二维码？
        } for activity in activities]
