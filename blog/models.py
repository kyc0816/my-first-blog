from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
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
