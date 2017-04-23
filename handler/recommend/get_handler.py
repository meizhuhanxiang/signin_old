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


class GetHandler(BaseHandler):
    @handler
    def post(self):
        commodity_id = self.get_json_argument('commodity_id')
        commodity_model = self.model_config.first(CommodityModel, id=commodity_id)  # type: CommodityModel
        recommend_models = self.model_config.all(RecommendModel,
                                                 commodity_id=commodity_model.id)  # type: RecommendModel
        recommends = []
        for recommend_model in recommend_models:  # type: RecommendModel
            user_model = self.model_config.first(UserModel, id=recommend_model.user_id, is_v=1)  # type: UserModel
            if user_model:
                recommends.append({
                    'profile': user_model.profile,
                    'name': user_model.name,
                    'job': user_model.job,
                    'is_v': user_model.is_v,
                    'content': recommend_model.content
                })
        return recommends
