#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from handler.base.base_handler import BaseHandler, handler
from model import ModelConfig
from model import CommodityModel
from model import PublisherModel
from model import RecommendModel
from model import UserModel
from model import OrderModel
from utils.exception import *


class AddHandler(BaseHandler):
    @handler
    def post(self):
        commodity_id = self.get_json_argument('commodity_id')
        content = self.get_json_argument('content')
        user_model = self.model_config.first(UserModel, id=self.session['user_id'], is_v=True)
        if not user_model:
            raise ServerError(ServerError.USER_NOT_V)
        recommend_models = self.model_config.all(RecommendModel, commodity_id=commodity_id, user_id=self.session['user_id'])
        if len(recommend_models) >= 5:
            raise ServerError(ServerError.RECOMMEND_TOO_MANY)
        else:
            recommend_model = RecommendModel(commodity_id=commodity_id, user_id=self.session['user_id'],
                                             content=content)  # type:CommodityModel
            self.model_config.add(recommend_model)
