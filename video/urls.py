from django.urls import path
from . import views

app_name="video"
urlpatterns=[
    path("introduce/",views.introduce_views,name="course_introduce"),
    path("course_video/",views.course_video,name="course_video"),
    path("detail<int:video_id>/",views.course_detail,name="video_detail"),
    path("token/",views.video_token)
]