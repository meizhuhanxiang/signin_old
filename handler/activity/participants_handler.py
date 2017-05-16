# -*- coding: utf-8 -*-

from model import ScoreModel, UserModel
from handler.base.base_handler import BaseHandler, handler


class ParticipantsHandler(BaseHandler):
    """ 获取活动信息 """
    @handler
    def post(self):
        activity_ids = self.get_json_argument('activity_ids')
        if activity_ids:
            res = self.session.query(ScoreModel.score, UserModel.nickname, UserModel.open_id, UserModel.sex,
                               UserModel.province, UserModel.profile, UserModel.name, UserModel.job, UserModel.company,
                               UserModel.phone, UserModel.email, UserModel.create_time)\
                .join(ScoreModel.user_id == UserModel.id).filter(ScoreModel.activity_id.in_(activity_ids)).all()
        else:
            res = self.session.query(ScoreModel.score, UserModel.nickname, UserModel.open_id, UserModel.sex,
                               UserModel.province, UserModel.profile, UserModel.name, UserModel.job, UserModel.company,
                               UserModel.phone, UserModel.email, UserModel.create_time)\
                .join(ScoreModel.user_id == UserModel.id).all()

        return [{
            'score': score,
            'nickname': nickname,
            'open_id': open_id,
            'sex': sex,
            'province': province,
            'profile': profile,
            'name': name,
            'job': job,
            'company': company,
            'phone': phone,
            'email': email,
            'create_time': create_time,
        } for score, nickname, open_id, sex, province, profile, name, job, company, phone, email, create_time in res]
