# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default='반려 동물 이름을 입력해주세요')
    text = models.TextField()
    breed = models.CharField(max_length=20, default='종을 입력해주세요')
    birthdate = models.CharField(max_length=20, default='출생 연도를 입력해주세요')
    ifneutralized = models.CharField(max_length=20, default='중성화 여부를 입력해주세요(함/안함)')
    ifvaccinatedrabies = models.CharField(max_length=30, default='광견병 백신 접종 여부를 입력해주세요(접종함/안함)')

    contact1 = models.CharField(max_length=30, default='비상연락망을 입력해주세요')
    contact2 = models.CharField(max_length=50, default='추가 비상연락망을 입력해주세요\n(없으시면 없음이라고 입력해주세요)')
    address = models.CharField(max_length=100, default='주소를 입력해주세요\n(없으시면 없음이라고 입력해주세요)')
    # 이 아래 줄이 비밀번호 땜에 추가한 것임
    password = models.CharField(max_length=4, default='0000')
    isFromDetailToEdit = models.CharField(max_length=1, default='0')  #이거 '0'으로 바꿔봤는데 에러나면 다시 그냥 0으로 바꾸기
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
