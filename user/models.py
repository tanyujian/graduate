from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from fernet_fields import EncryptedCharField,EncryptedEmailField
from mirage import fields
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self,email,username,password,**kwargs):
        if not email:
            raise ValueError("没有填写手机号码")
        if not username:
            raise ValueError("没有填写用户名")
        if not password:
            raise ValueError("没有填写密码")
        user=self.model(email=email,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return  user
    def create_user(self,email,username,password,**kwargs):
        kwargs["is_staff"]=False
        return self._create_user(email,username,password,**kwargs)
    def create_superuser(self,email,username,password,**kwargs):
        kwargs["is_staff"]=True
        kwargs["is_superuser"]=True
        return self._create_user(email,username,password,**kwargs)

class MyUser(AbstractBaseUser,PermissionsMixin):
    email = fields.EncryptedEmailField(blank=False,null=True,verbose_name='邮件')
    nickname= fields.EncryptedCharField( max_length=30,verbose_name='名字')
    username=models.CharField(unique=True,max_length=30,verbose_name='用户名')
    position=models.CharField(max_length=50,default="学生",verbose_name="职位")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    join_time=models.DateTimeField(auto_now_add=True)
    desc=models.TextField(blank=True,null=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ["email"]
    EMAIL_FIELD="email"
    objects=UserManager()
    def get_full_username(self):
        return self.username
    def get_short_username(self):
        return self.username
    def __str__(self):
        return self.nickname
