# -*- coding: utf-8 -*-

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # 아랫줄에서 password 지워야됨
        fields = ('title', 'breed', 'birthdate', 'ifneutralized', 'ifvaccinatedrabies', 'registrationnumber', 
        	'text', 'healthwarnings', 'ownername', 'contact1', 'contact2', 'address', 'password',)