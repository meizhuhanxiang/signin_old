#!/usr/bin/python
# -*- coding: utf-8 -*-

from model import PublisherModel
from handler.base.base_handler import BaseHandler, handler


class GetHandler(BaseHandler):
    @handler
    def post(self):
        publisher_ids = self.get_json_argument('publisher_ids')
        if publisher_ids:
            publishers = self.model_config.filter_all(PublisherModel,
                                                      filters=PublisherModel.id.in_(tuple(publisher_ids)))
        else:
            publishers = self.model_config.all(PublisherModel)

        return [{
            'publisher_id': publisher.id,
            'name': publisher.name,
            'brief_introduction': publisher.brief_introduction,
            'logo': publisher.logo,
            'address': publisher.address,
            'create_time': publisher.create_time,
            'update_time': publisher.update_time,
            'qr_code': ''  # TODO: 如何获取发布方的二维码？
        } for publisher in publishers]
