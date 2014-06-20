# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''
from utils.tools import render_and_response
from product.models import Item, Category
from django.http.response import Http404
from django.core.paginator import Paginator, InvalidPage


def home_page(req):
    cate = Category.objects.get_by_id(req.REQUEST.get('cate', '1'))
    if not cate:
        raise Http404
    items = cate.item_set.filter(is_active=True)
    paginator = Paginator(items, 22)
    page_num = req.REQUEST.get('p', '1')
    if not page_num.isdigit:
        page_num = int(page_num)
    try:
        result = paginator.page(page_num)
    except InvalidPage:
        result = paginator.page(1)
    return render_and_response(req, 'index.html', {'items': result, 'cate': cate,
                                                   'page': result})


def about(req):
    return render_and_response(req, 'about.html')


def idea(req):
    return render_and_response(req, 'idea.html')


def detail(req, id):
    item = Item.objects.get_by_id(id)
    cate = Category.objects.get_by_id(req.REQUEST.get('cate', '1'))
    if not item or not item.is_active or not cate or not cate in item.cate.all():
        raise Http404
    return render_and_response(req, 'product/detail.html', {'item': item,
                                                            'cate': cate})
