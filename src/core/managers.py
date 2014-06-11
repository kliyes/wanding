# -*-coding:utf-8 -*-
'''
Created on Jun 11, 2014

@author: tom <tom@kliyes.com>
'''

from django.db.models.manager import Manager


class BaseManager(Manager):
    def __init__(self):
        super(BaseManager, self).__init__()

    def get_by_id(self, id):
        try:
            return self.get(id=id)
        except Exception, e:
            print e
            return None
