# -*- coding:utf8 -*-
from __future__ import unicode_literals
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称')
    address = models.CharField(max_length=128, verbose_name='地址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name



