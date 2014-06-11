# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''

from django.db import models

from core.managers import BaseManager


class BaseModel(models.Model):
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ('-create_time',)
