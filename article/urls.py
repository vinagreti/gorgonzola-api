from rest_framework import routers
from article.views import *
from django.conf.urls import url

api_routes = routers.DefaultRouter()
api_routes.register(r'article', ArticleViewSet, base_name='article')

urlpatterns = api_routes.urls
