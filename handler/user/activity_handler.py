# -*- coding: utf-8 -*-

from model import ScoreModel, UserModel, ActivityModel
from handler.base.base_handler import BaseHandler, handler


class ActivityHandler(BaseHandler):
    """ 获取用户参与的活动信息 """
    @handler
    def post(self):
        user_ids = self.get_json_argument('user_ids')

        if user_ids:
            res = self.session.query(ScoreModel.score, UserModel.nickname, UserModel.open_id, UserModel.sex,
                                     UserModel.name, UserModel.phone, ActivityModel.content, ActivityModel.time,
                                     ActivityModel.place)\
                .join(ScoreModel.user_id == UserModel.id).join(ScoreModel.activity_id == ActivityModel.id)\
                .filter(ScoreModel.user_id.in_(user_ids)).all()
        else:
            res = self.session.query(ScoreModel.score, UserModel.nickname, UserModel.open_id, UserModel.sex,
                                     UserModel.name, UserModel.phone, ActivityModel.content, ActivityModel.time,
                                     ActivityModel.place) \
                .join(ScoreModel.user_id == UserModel.id).join(ScoreModel.activity_id == ActivityModel.id).all()

        return [{
            'score': score,
            'nickname': nickname,
            'open_id': open_id,
            'sex': sex,
            'name': name,
            'phone': phone,
            'activity': content,
            'activity_time': time,
            'activity_place': place
        } for score, nickname, open_id, sex, name, phone, content, time, place in res]
