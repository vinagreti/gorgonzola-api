# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from article.models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ['id', 'name']

admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    list_filter = ('id', 'name', 'color')
    search_fields = ['id', 'name', 'color']

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'category', 'title', 'content', 'thumb')
    list_filter = ('id', 'author', 'category', 'title', 'content', 'thumb')
    search_fields = ['id', 'author__name', 'category__name', 'title', 'content', 'thumb']

admin.site.register(Article, ArticleAdmin)