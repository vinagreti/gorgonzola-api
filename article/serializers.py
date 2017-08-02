from rest_framework import serializers
from rest_framework.authtoken.models import Token
from article.models import *

pic_folder = "pic_folder"

def GetImageLink(path, absolute_url):
    port_position = absolute_url.index('8000')
    api_host_end_at = absolute_url.index('api/v1')
    url_host = absolute_url[0:api_host_end_at]
    return "{0}{1}".format(
        url_host, path)

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'avatar']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'color']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    desc = serializers.SerializerMethodField()
    thumb = serializers.SerializerMethodField()

    def get_desc(self, instance):
        if len(instance.content) > 300:
            return instance.content[0:250] + "..."
        else:
            return instance.content

    def get_thumb(self, instance):
        request = self.context.get('request')
        return  GetImageLink(instance.thumb.url, request.build_absolute_uri())

    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'author', 'category', 'thumb']
