from django import forms
from django.core.cache import cache
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth import authenticate
from .models import MyUser


class LoginForm(forms.Form):
    username=forms.CharField(label="用户名",required=False,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"输入你的用户名"}))
    password=forms.CharField(label='密码',required=False,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"输入密码"}))
    captcha=CaptchaField(label="验证码")
    def clean(self):
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user= authenticate(username=username,password=password)
        self.cleaned_data["user"]=user
        if user is None:
            raise forms.ValidationError("用户名或密码错误")
        return self.cleaned_data


class RegisterForm(UserCreationForm):
    v_code=forms.CharField(label="验证码",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"输入验证码"}))
    class Meta:
        model=MyUser
        fields=["username","email","nickname"]
    def __init__(self,*args,**kwargs):
        if "request" in kwargs:
            self.request=kwargs.pop("request")
        super().__init__(*args, **kwargs)
    def clean(self):
        email_=self.cleaned_data.get("email")
        code=cache.get(email_)
        print("========")
        print(code)
        print("========")
        v_code=self.cleaned_data.get('v_code','').strip()
        if not(code == v_code and code !=''):
            raise  forms.ValidationError("验证码不正确")


#改变昵称表单
class ChangeNickname(forms.Form):
    nickname=forms.CharField(label="昵称",
                             widget=forms.TextInput(attrs={"class":"form_control","placeholder":"输入你的新昵称"}))

    def clean(self):
        nickname=self.cleaned_data.get("nickname",'').strip()
        if nickname == '':
            raise  forms.ValidationError("昵称不能为空")
        return self.cleaned_data
#改变邮箱表单
class ChangeEmail(forms.Form):
    email=forms.CharField(label='邮箱',
                          widget=forms.TextInput(attrs={"class":"form_control","placeholder":"输入邮箱地址"}))
    v_code=forms.CharField(label="验证码",
                           widget=forms.TextInput(attrs={"class":"form_control","placeholder":"输入验证码"}))
    def clean(self):
        email_=self.cleaned_data.get("email")
        code=cache.get(email_)
        v_code=self.cleaned_data.get("v_code","")
        if not(code !=''and code==v_code):
            raise  forms.ValidationError("验证码不正确")
        return self.cleaned_data
#修改密码
class ChangePassword(PasswordChangeForm):
    class Meta:
        model=MyUser
    # pass
