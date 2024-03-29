#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from handler.base.base_handler import BaseHandler, handler
import uuid
import utils.config
from utils.exception import *
from wechatpy.pay import WeChatPay
from wechatpy.pay.api import WeChatOrder
from utils.exception import ServerError
from traceback import format_exc
import re


class CheckloginHandler(BaseHandler):
    @handler
    def post(self):
        res = {"login": False}
        if self.session.get('user_id', ''):
            res["login"] = True
        return res
