# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, verbose_name='Author', on_delete=models.PROTECT)
    name = models.CharField(max_length=120)
    avatar = models.CharField(max_length=1024)

    def __str__(self):
        return str(self.user.username)


class Category(models.Model):
    name = models.CharField(max_length=48)
    color = models.CharField(max_length=7)

    def __str__(self):
        return str(self.name)

class Article(models.Model):
    author = models.ForeignKey(Author, verbose_name='Author', on_delete=models.PROTECT)
    category = models.ForeignKey(Category, verbose_name='Category', blank=True, on_delete=models.PROTECT)
    title = models.CharField(max_length=120)
    content = models.TextField()
    thumb = models.ImageField(upload_to = 'static/pic_folder/', default = 'static/pic_folder/None/no-img.jpg')