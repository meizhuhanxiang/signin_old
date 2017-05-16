# -*- coding: utf-8 -*-

import datetime

from model import UserModel
from handler.base.base_handler import BaseHandler, handler


class AddHandler(BaseHandler):
    """ 添加用户信息 """

    @handler
    def post(self):
        current_time = datetime.datetime.now()

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

        user = UserModel(nickname=nickname, open_id=open_id, sex=sex, province=province, city=city, country=country,
                         profile=profile, privilege=privilege, union_id=union_id, name=name, job=job, company=company,
                         phone=phone, email=email, is_del=False, create_time=current_time, update_time=current_time)
        self.model_config.add(user)
        return {'user_id': user.id}
