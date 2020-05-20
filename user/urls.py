from django.urls import path
from . import views

app_name="user"
urlpatterns=[
    path("",views.tech_tem,name="tech_tem"),
    path("login/",views.log_in,name="login"),
    path("signup/",views.sign_up,name="signup"),
    path("sendemail/",views.sendemail,name="sendemail"),
    path("logout/",views.log_out,name="logout"),
    path("personal/",views.personal,name="personal"),
    path("change_email/",views.change_email,name="change_email"),
    path("change_name/",views.change_nickname,name="change_nickname"),
    path("changePassword/",views.change_password,name="changePassword")
]