# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2014 Lianbi TECH Co., Ltd. All rights reserved.
# Created on Jun 18, 2014, by tom
#
#
from django.contrib import admin
from product.models import Pic, Tag, Category, Item
__author__ = 'tom'


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'used_count')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'used_count')


class PicInline(admin.TabularInline):
    model = Pic


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'like_count', 'is_active')
    list_editable = ('is_active',)
    filter_horizontal = ('tag', 'cate')
    inlines = [PicInline]

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
