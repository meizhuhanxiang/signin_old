# -*- coding: utf-8 -*-

import datetime

from model import ScoreModel
from handler.base.base_handler import BaseHandler, handler


class AddHandler(BaseHandler):
    """ 为活动参与者添加分数 """

    @handler
    def post(self):
        current_time = datetime.datetime.now()

        user_id = self.get_json_argument('user_id')
        activity_id = self.get_json_argument('activity_id')
        score = self.get_json_argument('score')
        comment = self.get_json_argument('comment')

        score = ScoreModel(user_id=user_id, activity_id=activity_id, score=score, comment=comment, is_del=False,
                           create_time=current_time, update_time=current_time)
        self.model_config.add(score)
        return {'score_id': score.id}
