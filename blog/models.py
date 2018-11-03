# -*- coding: utf-8 -*- 

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title = models.CharField(max_length=20, default='반려 동물 이름을 입력해주세요')
    # text = models.TextField(default='반려 동물의 특이 사항을 입력해주세요\n예) 입 주변을 만지면 물 수 있으니 조심해주세요 등')
    # healthwarnings = models.TextField(default='반려 동물의 건강상의 주의 사항을 입력해주세요\n예) 쿠싱 증후군입니다. 수술 마취시 주의해야합니다 등\n건강상의 주의 사항은 반려동물의 실종 당시(보호자 부재시) 생길 수 있는\n사고, 질병 상황을 대비하여 의료진 및 임시 보호자에게 알리기 위함입니다.')
    # breed = models.CharField(max_length=20, default='종을 입력해주세요')
    # birthdate = models.CharField(max_length=20, default='yyyy-mm-dd')
    # ifneutralized = models.CharField(max_length=20, default='중성화 여부를 입력해주세요')
    # ifvaccinatedrabies = models.CharField(max_length=30, default='광견병 백신 접종 여부를 입력해주세요')
    # registrationnumber = models.CharField(max_length=100, default='반려동물 등록번호를 입력해주세요')

    # ownername = models.CharField(max_length=20, default='주인 이름을 입력해주세요')
    # contact1 = models.CharField(max_length=30, default='비상연락망을 입력해주세요')
    # contact2 = models.CharField(max_length=50, default='추가 비상연락망을 입력해주세요')
    # address = models.CharField(max_length=100, default='주소를 입력해주세요')
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
