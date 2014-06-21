# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''

from django.shortcuts import render_to_response
from django.template.context import RequestContext


def render_and_response(req, t, data={}):
    return render_to_response(t, RequestContext(req, data))


def get_ip(req):
    return req.META.get('HTTP_X_FORWARDED_FOR') or req.META.get('REMOTE_ADDR')
