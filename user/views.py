from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.cache import cache
from django.contrib.auth import logout,login,authenticate,get_user_model
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.http import JsonResponse
from .forms import LoginForm,RegisterForm,ChangeNickname,ChangeEmail,ChangePassword
import string
import random

from .models import MyUser

# Create your views here.

def tech_tem(request):
    teacher=MyUser.objects.filter(is_staff=True)[:8]
    content={"teacher":teacher}
    return render(request,"tech_tem.html",content)

#退出
def log_out(request):
    logout(request)
    return redirect("index")
#登陆
def log_in (request):
    content = {}
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data["user"]
            login(request,user)
            return redirect('index')
    else:
        form=LoginForm()
    content["title"]="登陆"
    content["send"]=""
    content["nature"]="hidden"
    content["forms"]=form
    return render(request,'user/Login.html',content)
#注册
def sign_up(request):
    content = {}
    if request.method=="POST":
        form=RegisterForm(request.POST,request=request)
        if form.is_valid():
            form.save()
            user=authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
            user.email=form.cleaned_data["email"]
            user.nickname=form.cleaned_data["nickname"]
            login(request,user)
            return redirect("index")
    else:
        form=RegisterForm()
    content["title"]="注册"
    content["send"]="发送验证码"
    content["nature"]=""
    content["forms"]=form
    return render(request,'user/Login.html',content)
#发送邮件
def sendemail(request):
    data={}
    email=request.GET.get("email")
    print("===========")
    print(email)
    print("===========")
    User=get_user_model()
    if User.objects.filter(email=email).exists():
        data["success"]="此邮箱已存在"
        return JsonResponse(data)
    code=''.join(random.sample(string.digits+string.ascii_letters,6))
    cache.set(email,code,600)
    send_mail(
        '邮箱验证',
        '验证码：%s' %code,
        '1277466401@qq.com',
        [email],
        fail_silently=False,
    )
    data["success"]="发送成功"
    return JsonResponse(data)

def change_nickname(request):
    content={}
    if request.method=="POST":
        form=ChangeNickname(request.POST)
        previous = request.GET.get("from",reverse("index"))
        if form.is_valid():
            User=get_user_model()
            user=User.objects.get(username=request.user.username)
            user.nickname=form.cleaned_data["nickname"]
            user.save()
            return redirect(previous)
    else:
        form=ChangeNickname()
    content["title"]="修改昵称"
    content["send"]=""
    content["nature"]="hidden"
    content["forms"]=form
    return render(request,'user/Login.html',content)
#改变邮箱
def change_email(request):
    content = {}
    if request.method=="POST":
        form=ChangeEmail(request.POST)
        if form.is_valid():
            User=get_user_model()
            user=User.objects.get(username=request.user.username)
            user.email=form.cleaned_data["email"]
            user.save()
            return redirect("index")
    else:
        form=ChangeEmail()
    content["title"]="修改"
    content["send"]="发送验证码"
    content["nature"]=""
    content["forms"]=form
    return render(request,'user/Login.html',content)

def change_password(request):
    content={}
    if request.method=="POST":
        form =ChangePassword(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form=ChangePassword(user=request.user)
    content["title"]="修改密码"
    content["send"]=""
    content["nature"]="hidden"
    content["forms"]=form
    return render(request,"user/Login.html",content)

def personal(request):
    return render(request,"user/personal.html")