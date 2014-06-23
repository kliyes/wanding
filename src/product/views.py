# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''
from utils.tools import render_and_response, get_ip
from product.models import Item, Category, LikeRecord, Tag
from django.http.response import Http404, HttpResponse
from django.core.paginator import Paginator, InvalidPage
import json
from django.db import transaction
import settings
from django.db.models.query_utils import Q


def pager(req, items):
    paginator = Paginator(items, settings.PAGE_SIZE)
    page_num = req.REQUEST.get('p', '1')
    if not page_num.isdigit:
        page_num = int(page_num)
    try:
        result = paginator.page(page_num)
    except InvalidPage:
        result = paginator.page(1)
    liked = LikeRecord.objects.filter(ip=get_ip(req)).values_list('item', flat=True)
    liked = Item.objects.filter(id__in=liked)
    return {'result': result, 'liked': liked}


def home_page(req):
    cate = Category.objects.get_by_id(req.REQUEST.get('cate', '1'))
    if not cate:
        raise Http404
    items = cate.item_set.filter(is_active=True)
    pager_result = pager(req, items)
    return render_and_response(req, 'index.html', {'items': pager_result['result'],
        'cate': cate, 'page': pager_result['result'],
        'liked': pager_result['liked']})


def search(req):
    k = req.REQUEST.get('k')
    tags = Tag.objects.filter(name__contains=k)
    items = Item.objects.filter(Q(Q(name__contains=k) | Q(brand__contains=k) |
        Q(material__contains=k) | Q(tag__in=tags)),
        is_active=True).distinct().order_by('rank')
    pager_result = pager(req, items)
    return render_and_response(req, 'index.html', {'items': pager_result['result'],
        'page': pager_result['result'], 'liked': pager_result['liked'],
        'from': 'search'})


def serch_tag(req):
    tid = req.REQUEST.get('tid')
    tag = Tag.objects.get_by_id(tid)
    if not tag:
        raise Http404
    items = tag.item_set.filter(is_active=True).order_by('rank')
    pager_result = pager(req, items)
    return render_and_response(req, 'index.html', {'items': pager_result['result'],
        'page': pager_result['result'], 'liked': pager_result['liked'],
        'from': 'search'})


def about(req):
    return render_and_response(req, 'about.html')


def idea(req):
    return render_and_response(req, 'idea.html')


def detail(req, id):
    item = Item.objects.get_by_id(id)
    cate = Category.objects.get_by_id(req.REQUEST.get('cate', '1'))
    if not item or not item.is_active or not cate or not cate in item.cate.all():
        raise Http404
    liked = LikeRecord.objects.filter(ip=get_ip(req)).values_list('item', flat=True)
    liked = Item.objects.filter(id__in=liked)
    return render_and_response(req, 'product/detail.html', {'item': item,
        'cate': cate, 'liked': liked})


@transaction.commit_on_success
def like(req):
    item = Item.objects.get_by_id(req.REQUEST.get('id'))
    if not item:
        return HttpResponse(json.dumps({'status': 0, 'msg': u'该产品不存在'}))
    LikeRecord.objects.get_or_create(ip=get_ip(req), item=item)
    item.like_count += 1
    item.save()
    return HttpResponse(json.dumps({'status': 1, 'msg': u'喜欢成功'}))
