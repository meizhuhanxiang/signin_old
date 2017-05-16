# -*- coding: utf-8 -*-

import datetime

from utils.exception import *
from model import UserModel
from handler.base.base_handler import BaseHandler, handler


class ModifyHandler(BaseHandler):
    """ 修改用户信息 """

    @handler
    def post(self):
        user_id = self.get_json_argument('user_id')
        nickname = self.get_json_argument('nickname')
        open_id = ''  # TODO: 前端传open_id？还是后端获取？
        sex = self.get_json_argument('sex')
        province = self.get_json_argument('province')
        city = self.get_json_argument('city')
        country = self.get_json_argument('country')
        profile = self.get_json_argument('profile')
        privilege = self.get_json_argument('privilege')
        union_id = self.get_json_argument('union_id')
        name = self.get_json_argument('name')
        job = self.get_json_argument('job')
        company = self.get_json_argument('company')
        phone = self.get_json_argument('phone')
        email = self.get_json_argument('email')

        user = self.model_config.first(UserModel, id=user_id)
        if not user:
            raise ServerError(ServerError.NOT_EXIST, args=user_id)

        if not [user.nickname, user.open_id, user.sex, user.province, user.city, user.country, user.profile,
                user.privilege, user.union_id, user.name, user.job, user.company, user.phone, user.email] == \
            [nickname, open_id, sex, province, city, country, profile, privilege, union_id, name, job, company, phone,
             email]:
            user.nickname = nickname
            user.open_id = open_id
            user.sex = sex
            user.province = province
            user.city = city
            user.country = country
            user.profile = profile
            user.privilege = privilege
            user.union_id = union_id
            user.name = name
            user.job = job
            user.company = company
            user.phone = phone
            user.email = email
            user.update_time = datetime.datetime.now()
            self.model_config.commit()
        return ''
