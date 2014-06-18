# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2014 Lianbi TECH Co., Ltd. All rights reserved.
# Created on Jun 18, 2014, by tom
#
#
__author__ = 'tom'

from product.models import Category


def cates(req):
    return {'cates': Category.objects.all(), 'current': req.REQUEST.get('cate')}
