# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20181103_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='주소를 입력해주세요 (선택)', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='birthdate',
            field=models.CharField(default='yyyy-mm-dd', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='breed',
            field=models.CharField(default='종을 입력해주세요', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='contact1',
            field=models.CharField(default='비상연락망을 입력해주세요 (필수)', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='contact2',
            field=models.CharField(default='추가 비상연락망을 입력해주세요 (선택)', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='healthwarnings',
            field=models.TextField(default='반려 동물의 건강상의 주의 사항을 입력해주세요\n예) 쿠싱 증후군입니다. 수술 마취시 주의해야합니다 등\n건강상의 주의 사항은 반려동물의 실종 당시(보호자 부재시) 생길 수 있는\n사고, 질병 상황을 대비하여 의료진 및 임시 보호자에게 알리기 위함입니다.'),
        ),
        migrations.AddField(
            model_name='post',
            name='ifneutralized',
            field=models.CharField(default='중성화 여부를 입력해주세요', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='ifvaccinatedrabies',
            field=models.CharField(default='광견병 백신 접종 여부를 입력해주세요', max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='ownername',
            field=models.CharField(default='주인 이름을 입력해주세요 (선택)', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='registrationnumber',
            field=models.CharField(default='반려동물 등록번호를 입력해주세요', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='반려 동물의 특이 사항을 입력해주세요\n예) 입 주변을 만지면 물 수 있으니 조심해주세요 등'),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='반려 동물 이름을 입력해주세요', max_length=20),
        ),
    ]