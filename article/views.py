# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import json 

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from article.models import *
from article.serializers import *

PAGE_SIZE = 6

class Pagination2000(PageNumberPagination):
    page_size = PAGE_SIZE

def GetArticlesByCategory(request, category):
    categories = Category.objects.filter(name=category)
    
    if categories:
        articles = Article.objects.filter(category__in=categories)[0:PAGE_SIZE]
        articles = ArticleSerializer(articles, many=True).data
    else:
        articles = []

    return HttpResponse(json.dumps({"results": articles}), content_type="application/json")

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    pagination_class = Pagination2000

    def get_queryset(self):
        queryset = Article.objects.all().order_by('-id')

        category = self.request.query_params.get('category', None)

        if category is not None:
            categories = Category.objects.filter(name=category)
            if categories:
                queryset = queryset.filter(category__in=categories)
            else:
                queryset = [];

        return queryset