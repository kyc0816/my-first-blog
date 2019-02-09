# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.http import Http404, HttpResponseNotFound, HttpResponse, StreamingHttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage

def post_list(request):
    # posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html')
    	# , {'posts': posts}

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post.isFromDetailToEdit)
	# 이 아래로 주석임  
    if request.method == "POST":
    	password = request.POST['password']
    	realpassword = post.password
    	if password == realpassword:
    		post.isFromDetailToEdit = '1'
    		post.save()
    		form = PostForm(instance=post)
    		return redirect('post_edit', pk=post.pk)
    		# return render(request, 'blog/post_edit.html', {'form': form}) 이건 틀린거였다. 뭔가 윗줄로 하면 안될 것 같은데 작동은 하네...
    	else:
    		messages.info(request, '비밀번호가 틀렸습니다')
    		return redirect('post_detail', pk=post.pk)
    # 이 위로 주석임
    else:
    	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        for i in range(100):
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                # post.breed                    //직접 입력하는게 아님
                # post.birthdate
                # post.ifneutralized
                # post.ifvaccinatedrabies
                post.isFromDetailToEdit = '0'
                post.save()
        return redirect('post_detail', pk=post.pk)
    else: #url 통해서 직접 오거나 +버튼 눌러서 오는 경우이다.
        form = PostForm()
        print(request.user)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user		user이 justin, 즉 admin이어야만 들어올 수 있어서 일단 들어온 담에 글을 쓰면 자동으로 justin으로 됐는데
            # 								   이제는 admin 아니어도 쓸 수 있게 됐는데 user를 따로 구현을 안했기에 이거를 그냥 비워둬야한다.
            # 								   애초에 글을 admin이 처음에 써놓고 사용자는 수정만 하게 해놔서 author는 전부 justin으로 남는다.
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
    	if post.isFromDetailToEdit == '1':    #아놔 그냥 1이라고 해놨어서 에러 계속 떴는데 '1'이네... 1시간 날렸다
    		form = PostForm(instance=post)
    		post.isFromDetailToEdit = '0'
    		post.save()
    		return render(request, 'blog/post_edit.html', {'form': form})
    	else:
    		raise Http404('Session Expired')

# 주석 111
# 아래는 NFC를 찍어서 urls.py의 url(r'^frmonfc/(?P<pk>\d+)/$'를 거치게 되었을 때 오게 되는 뷰이다. 받은 pk의 글이 있으면 post_detail로 보내고
# 없으면 post_new로 보낼 것이다...... 아 근데 이렇게 하면 큰 문제가 있다. pk=15인 NFC로 들어와서 new로 글을 쓰면 그 글을 쓴 순서에 따라 글의
# pk는 23 이렇게 설정될 수도 있다. 그러면 글을 만든 뒤에 나중에 찍었을 때 pk=15인 글의 post_detail을 불러오기 때문에 엉뚱한 강아지를 보여준다.
# 이거를 하려면 post 말고 user 모델이 필수적으로 있어야한다. 겁나 복잡하다... 

@csrf_exempt
def service_learning(request):
    if request.method == "POST":
        received_json_data = request.body.decode('utf-8')
        # data = request.body.decode('utf-8')
        # received_json_data = json.loads(data)
        # received_GPS = received_json_data.get("GPS")
        print('bad')
        print(received_GPS)
        email = EmailMessage('GPS Coordinate is ', received_GPS, to=['katejohnsonfromkenya@gmail.com'])
        email.send()
        return StreamingHttpResponse('it was post request: '+str(received_json_data))
    else:
        print('good')
        return StreamingHttpResponse('it was GET request')
