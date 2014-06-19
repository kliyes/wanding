# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2014 Lianbi TECH Co., Ltd. All rights reserved.
# Created on Jun 18, 2014, by tom
#
#
import settings
__author__ = 'tom'

from product.models import Category


def cates(req):
    current = req.REQUEST.get('cate', '1')
    if not current.isdigit():
        current = 1
    current = int(current)
    return {'cates': Category.objects.all(), 'current': current}


def forum(req):
    return {'forum': settings.FORUM_URL}
