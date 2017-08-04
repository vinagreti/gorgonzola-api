from rest_framework import serializers
from rest_framework.authtoken.models import Token
from article.models import *

pic_folder = "pic_folder"

def GetImageLink(path):
    return path

class AuthorSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name', 'avatar']

    def get_avatar(self, instance):
        request = self.context.get('request')
        return  GetImageLink(instance.avatar.url)


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
        return  GetImageLink(instance.thumb.url)

    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'author', 'category', 'thumb']
