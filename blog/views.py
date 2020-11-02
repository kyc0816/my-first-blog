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

def service_learning(request):
    if request.method == 'GET':
        print('well..')
        #2020 1102.. 결국 여기로 다시 왔다.. 시도해본다
        EmailMessage('Hello', 'Hello Flask message sent from Flask-Mail', to=['youngcheol33@gmail.com']).send()
        return "Sent"

    # try:
    #     if request.method == "POST":
    
    #         # **** dataType = string && REAL CODE
    #         received_string = request.body.decode('utf-8')      # received_string be like --> ID + Button + Lat(32.2576) + Lon(136.2345)
    
    
    #         #2020-10-20 내 종설 때문에 다시 바꾼 코드 (여기까지 오긴 오나해서 써놨다.. 뭐가 문젠지 보려고. 임시로 여기 있는 애다.)
    #         EmailMessage('충전 요청', 'hi', to=['youngcheol33@gmail.com']).send() # --> 실행 안되는걸로 판명..
    
    #         if received_string[0]=='1':                         # Min-Su's ID is 1
    #         #2020-10-20 내 종설 때문에 다시 바꾼 코드
    #             emer_kid_parent_email = 'youngcheol33@gmail.com'
    
    #         #경민이 종설 때문에 바꾼 코드 --> 무력화시킴
    #             # emer_kid_name = '김민수'
    #             # emer_kid_parent_email = 'jinrudals135@gmail.com'
    #             # emer_kid_age = '15'
    #             # emer_kid_school = '서울중학교'
    #             # emer_kid_class = '2학년 3반'
    #             # emer_kid_past_bullied_record = '있음'
    
    #         #경민이 종설 때문에 바꾼 코드 --> 무력화시킴
    #         # # GPS lat&lon extraction
    #         # received_lat = received_string[2:9]
    #         # received_lon = received_string[9:]
    #         # # email body in common
    #         # email_body = emer_kid_school + emer_kid_name + ' 학생이 학교 폭력 신고 장치를 통해 도움을 요청하였습니다.\n\n아래 링크를 통해 신고 위치를 확인하십시오.\n\n\n\n' + 'https://www.google.com/maps/search/?api=1&query=' + received_lat + ',' + received_lon + '\n\n\n'
    
    #         #경민이 종설 때문에 바꾼 코드
    #         email_body = '배터리가 부족합니다.\n 충전해주세요'
    
    #         #경민이 종설 때문에 바꾼 코드 --> 무력화시킴
    #         # e-mail to parents
    #         # email_parents = EmailMessage('귀하의 자녀 ' + emer_kid_name + '(으)로부터 도움 요청', email_body, to=[emer_kid_parent_email])
    
    #         #경민이 종설 때문에 바꾼 코드
    #         # email_parents = EmailMessage('충전 요청', email_body, to=[emer_kid_parent_email])
    #         #2020-10-20 내 종설 때문에 다시 바꾼 코드
    #         email_parents = EmailMessage('충전 요청', email_body, to=[emer_kid_parent_email])
    
    #         email_parents.send()
    
    #         #경민이 종설 때문에 바꾼 코드 --> 무력화시킴
    #         # e-mail to police
    #         # if received_string[1]=='1':
    #         #     # to Police --> add kid information to common email body.
    #         #     emer_kid_info = '학생 정보 :\n\n' + '이름 : ' + emer_kid_name + '\n' + '나이 : ' + emer_kid_age + '\n' + '학교 : ' + emer_kid_school + '\n' + '학급 : ' + emer_kid_class + '\n' + '학교 폭력 피해 전력 : ' + emer_kid_past_bullied_record
    
    #         #     email_police = EmailMessage('학교 폭력 신고가 발생하였습니다.', email_body + emer_kid_info, to=['katejohnsonfromkenya@gmail.com'])
    #             # email_police.send()
    
    
    #         # # **** dataType = string && test code(Just sends the string itself)
    #         # received_string = request.body.decode('utf-8')
    #         # if received_string[0]=='1':
    #         #     email_police = EmailMessage('학교 폭력 신고가 발생하였습니다.', received_string, to=['katejohnsonfromkenya@gmail.com'])
    #         #     email_police.send()
    
    
    
    
    
    
    #         # **** dataType = JSON
    #         # data = request.body.decode('utf-8')
    #         # received_json_data = json.loads(data)
    #         # # received_GPS = received_json_data.get("GPS")
    #         # received_ID = received_json_data.get("ID")
    #         # received_button1 = received_json_data.get("button1")
    #         # received_button2 = received_json_data.get("button2")
    #         # received_latitude = received_json_data.get("latitude")
    #         # received_longitude = received_json_data.get("longitude")
    #         # email = EmailMessage('Data is ', received_ID+received_button1+received_button2+received_latitude+received_lonigutde, to=['jinrudals135@gmail.com'])
    #         # email.send()
    
    
    
    #         # **debug
    #         # print('bad')
    #         # print(received_GPS)
    
            
    
    #         # **** response = StreamingHttpResponse
    #         # return StreamingHttpResponse('it was post request: '+str(received_json_data))
    
    #         # **** response = HttpResponse
    #         return HttpResponse('it was post request')
    
            
    
    
    #     else:
    #         # **debug
    #         # print('good')
    
    #         # **** response = StreamingHttpResponse
    #         # return StreamingHttpResponse('it was GET request')
    
    #         # **** response = HttpResponse
    #         return HttpResponse('it was GET request')
    # except:
    #     return HttpResponse("it didn't even go through if statement")