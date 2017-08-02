from rest_framework import serializers
from rest_framework.authtoken.models import Token
from article.models import *

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

    def get_desc(self, instance):
        if len(instance.content) > 300:
            return instance.content[0:250] + "..."
        else:
            return instance.content

    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'author', 'category', 'thumb']
