from django.conf.urls import url
from rest_framework import routers
from article.views import *

api_routes = routers.DefaultRouter()
api_routes.register(r'article', ArticleViewSet, base_name='article')

urlpatterns = [
    url(r'^article/(?P<category>[a-z A-Z]+)/', GetArticlesByCategory),
]

urlpatterns += api_routes.urls