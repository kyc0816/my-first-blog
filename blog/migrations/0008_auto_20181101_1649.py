# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181101_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ownername',
            field=models.CharField(default='주인 이름을 입력해주세요', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(default='특이 사항이나 주의 사항을 입력해주세요'),
        ),
    ]