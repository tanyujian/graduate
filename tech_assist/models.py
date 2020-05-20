from django.db import models
from video.models import CourseVideo
from user.models import MyUser
# Create your models here.

class TechFile(models.Model):
    file=models.FileField()
    desc=models.CharField(max_length=100)
    video=models.ForeignKey(CourseVideo,on_delete=models.CASCADE)
    class Meta:
        verbose_name="教学课件"

class TechWork(models.Model):
    file=models.FileField()
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    course=models.ForeignKey(CourseVideo,on_delete=models.CASCADE)
    class Meta:
        verbose_name="教学作业"

class CourseGrate(models.Model):
    grate=models.IntegerField(default=0)
    work=models.ForeignKey(TechFile,on_delete=models.CASCADE)
    class Meta:
        verbose_name="成绩"
