from django.contrib import admin
from .models import CourseVideo
# Register your models here.

class CourseV(admin.ModelAdmin):
    list_display = ["title","teacher","price","pub_time"]

admin.site.register(CourseVideo,CourseV)