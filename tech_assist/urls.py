from django.urls import path
from .import views

app_name="tech_assist"
urlpatterns=[
    path("condition/",views.tech_condition,name="conditions"),
    path("outline/",views.the_outline,name="outline"),
    path("load/<int:course_id>",views.load_course_file,name="load"),
    path("send-file/",views.send_work,name="send-file")
]