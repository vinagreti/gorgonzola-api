# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-03 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20170802_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='article.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(default='static/pic_folder/None/no-img.jpg', upload_to='static/pic_folder/'),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='static/pic_folder/None/no-img.jpg', upload_to='static/pic_folder/'),
        ),
    ]