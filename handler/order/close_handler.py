#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import datetime
from handler.base.base_handler import BaseHandler, handler
from model import OrderModel


class CloseHandler(BaseHandler):
    @handler
    def post(self):
        order_ids = self.get_json_argument('order_ids')
        delete = self.get_json_argument('delete', default=False, allow_null=True)
        order_models = self.model_config.filter_all(OrderModel, user_id=self.session['user_id'],
                                                    filters=OrderModel.id.in_(tuple(order_ids)))
        for order_model in order_models:  # type:OrderModel
            if str(delete).lower() == 'true':
                order_model.is_del = True
            current_status = order_model.status
            order_model.status = OrderModel.STATUS_CLOSE
            order_model.close_type = current_status
            order_model.close_time = datetime.datetime.now()
        self.model_config.commit()
