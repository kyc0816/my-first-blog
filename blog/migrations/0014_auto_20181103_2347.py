# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 14:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20181103_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='address',
        ),
        migrations.RemoveField(
            model_name='post',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='post',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='post',
            name='contact1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='contact2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='healthwarnings',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ifneutralized',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ifvaccinatedrabies',
        ),
        migrations.RemoveField(
            model_name='post',
            name='ownername',
        ),
        migrations.RemoveField(
            model_name='post',
            name='registrationnumber',
        ),
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]