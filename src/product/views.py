# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''
from utils.tools import render_and_response
from product.models import Item, Category
from django.http.response import Http404


def home_page(req):
    return render_and_response(req, 'index.html')


def about(req):
    return render_and_response(req, 'about.html')


def idea(req):
    return render_and_response(req, 'idea.html')


def detail(req, cate, id):
    item = Item.objects.get_by_id(id)
    cate = Category.objects.get_by_id(cate)
    if not item or not item.is_active or not cate or not cate in item.cate.all():
        raise Http404
    return render_and_response(req, 'product/detail.html', {'item': item,
                                                            'cate': cate})
