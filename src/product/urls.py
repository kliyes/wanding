# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''

from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^(\d+)/$', 'product.views.detail', name='detail'),
)
