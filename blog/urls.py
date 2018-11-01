# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    # 아래는 NFC를 찍고 왔을 때 처음 가게 되는 view의 url. 글이 이미 있다면 post_detail로 보낼거고 아니면 new로 보내야된다.
    # 그리고 이 링크를 통하지 않고는 new로 올 수 없게 해야한다.      아 근데 문제가 있다. User 구현하기 전에는 이거 못한다. 자세한 사항은
    # views.py에서 65번째 줄쯤 있는 "주석 111"을 봐라... User 아니면 적어도 뭐 AuthCode 이런거라도 구현해야한다.

    # url(r'^frmonfc/(?P<pk>\d+)/$', views.from_nfc, name='from_nfc'),
]