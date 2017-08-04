# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TransactionTestCase 

# Create your tests here.
from article.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import transaction

import tempfile

class ArticleTestCase(TransactionTestCase):

    # ARTICLES SETUP
    def setupArticle(self):
        Article.objects.create(author=self.author, category=self.category, title="article1", content="content", thumb=self.image) # normal creation
        Article.objects.create(author=self.author, category=self.category, title="article2", content="content") # auto add thumb


    # AUTHOR SETUP
    def setupAuthor(self):
        Author.objects.create(user=self.user, name="author1", avatar=self.image) # normal creation
        Author.objects.create(user=self.user, name="author2") # auto add avatar


    # CATEGORY SETUP
    def setupCategory(self):
        Category.objects.create(name="category1", color="#fff") # normal creation


    # MAIN SETUP
    def setUp(self):
        # GLOBALS
        self.image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        self.user = User.objects.create(username="setUp", password="setUp")
        self.category = Category.objects.create(name="setUp", color="#fff")
        self.author = Author.objects.create(user=self.user, name="setUp", avatar=self.image)

        # MODELS
        self.setupAuthor()
        self.setupArticle()
        self.setupCategory()


    # ARTICLES
    def test_article_should_create(self):
        article1 = Article.objects.get(title="article1")
        article2 = Article.objects.get(title="article2")
        self.assertIsInstance(article1, Article)
        self.assertIsInstance(article2, Article)


    def test_article_should_not_create_without_required_fields(self):

        # no TITLE raises ValidationError
        try:
            a = Article.objects.create(author=self.author, category=self.category, content="content", thumb=self.image)
            a.clean_fields()
        except ValidationError:
            pass

        # no CONTENT raises ValidationError
        try:
            a = Article.objects.create(author=self.author, category=self.category, title="title", thumb=self.image)
            a.clean_fields()
        except ValidationError:
            pass

        # no AUTHOR raises IntegrityError
        try:
            a = Article.objects.create(category=self.category, title="title", content="content", thumb=self.image)
            a.clean_fields()
        except IntegrityError:
            pass

        # no CATEGORY raises IntegrityError
        try:
            a = Article.objects.create(author=self.author, title="title", content="content", thumb=self.image)
            a.clean_fields()
        except IntegrityError:
            pass


    # AUTHOR
    def test_author_should_create(self):
        author1 = Author.objects.get(name="author1")
        author2 = Author.objects.get(name="author2")
        self.assertIsInstance(author1, Author)
        self.assertIsInstance(author2, Author)


    def test_author_should_not_create_without_required_fields(self):
        # no NAME raises ValidationError
        try:
            a = Author.objects.create(user=self.user, avatar=self.image)
            a.clean_fields()
        except ValidationError:
            pass

        # no USER raises IntegrityError
        try:
            a = Author.objects.create(name="author1", avatar=self.image)
            a.clean_fields()
        except IntegrityError:
            pass


    # CATEGORY
    def test_category_should_create(self):
        category1 = Category.objects.get(name="category1")
        self.assertIsInstance(category1, Category)


    def test_category_should_not_create_without_required_fields(self):
        # no COLOR raises ValidationError
        try:
            a = Category.objects.create(name="name")
            a.clean_fields()
        except ValidationError:
            pass