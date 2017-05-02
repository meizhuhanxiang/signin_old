#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from handler.base.base_handler import BaseHandler, handler
import uuid
import utils.config
from utils.exception import *
from wechatpy.pay import WeChatPay
from wechatpy.pay.api import WeChatOrder
from wechatpy.oauth import WeChatOAuth
from model import UserModel
import urllib


class RegisteHandler(BaseHandler):
    @handler
    def post(self):
        user_id = self.get_json_argument('user_id')
        name = self.get_json_argument('name')
        job = self.get_json_argument('job')
        company = self.get_json_argument('company')
        phone = self.get_json_argument('phone')
        email = self.get_json_argument('email')

        user_model = self.model_config.first(UserModel, id=user_id)  # type:UserModel
        if user_model:
            user_model.name = name
            user_model.job = job
            user_model.company = company
            user_model.phone = phone
            user_model.email = email
            self.model_config.commit()
        else:
            raise ServerError(ServerError.USER_ID_NO_EXIST, args=user_id)
