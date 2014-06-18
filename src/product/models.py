# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''
from django.db import models

from core.models import BaseModel
import settings


class Tag(BaseModel):
    name = models.CharField(u'名称', max_length=16)

    def __unicode__(self):
        return self.name

    def used_count(self):
        return self.item_set.filter(is_active=True).count()

    class Meta:
        verbose_name = u'关键词'
        verbose_name_plural = u'关键词'


class Category(BaseModel):
    name = models.CharField(u'名称', max_length=16)

    def __unicode__(self):
        return self.name

    def used_count(self):
        return self.item_set.filter(is_active=True).count()

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'


class Item(BaseModel):
    name = models.CharField(u'名称', max_length=128)
    price = models.FloatField(u'价格', default=0.0)
    like_count = models.IntegerField(u'喜欢人数', default=0)
    brand = models.CharField(u'品牌', max_length=32, null=True, blank=True)
    weight = models.CharField(u'重量', max_length=8, null=True, blank=True)
    product_size = models.CharField(u'产品尺寸', max_length=32, null=True, blank=True)
    package_size = models.CharField(u'包装尺寸', max_length=32, null=True, blank=True)
    material = models.CharField(u'材质', max_length=32, null=True, blank=True)
    tag = models.ManyToManyField(Tag, verbose_name=u'关键词', null=True, blank=True)
    cate = models.ManyToManyField(Category, verbose_name=u'分类', null=True, blank=True)
    rank = models.IntegerField(u'排序', default=1)
    is_active = models.BooleanField(u'发布', default=False)

    def __unicode__(self):
        return self.name

    def get_show_pics(self):
        return self.pic_set.filter(type='S')

    def get_desc_pics(self):
        return self.pic_set.filter(type='D')

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = u'产品'
        ordering = ('rank',)


PIC_TYPE = (
    ('S', u'展示图片'),
    ('D', u'描述图片'),
)


class Pic(BaseModel):
    name = models.CharField(u'名称', max_length=16, null=True, blank=True)
    item = models.ForeignKey(Item, verbose_name=u'产品', null=True, blank=True)
    pic = models.ImageField(u'图片', upload_to=settings.ITEM_PIC_FOLDER, null=True, blank=True)
    type = models.CharField(u'类型', max_length=1, choices=PIC_TYPE, default='D')
    rank = models.IntegerField(u'排序', default=1)

    def __unicode__(self):
        return self.name or ""

    class Meta:
        verbose_name = u'产品图片'
        verbose_name_plural = u'产品图片'
        ordering = ('type', 'rank')
