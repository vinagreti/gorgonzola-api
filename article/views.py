# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from article.models import *
from article.serializers import *
from rest_framework.pagination import PageNumberPagination

class Pagination2000(PageNumberPagination):
    page_size = 6

    
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-id')
    serializer_class = ArticleSerializer
    pagination_class = Pagination2000