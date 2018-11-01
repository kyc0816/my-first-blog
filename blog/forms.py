from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # 아랫줄에서 password 지워야됨
        fields = ('title', 'breed', 'birthdate', 'ifneutralized', 'ifvaccinatedrabies', 'text', 'password',)