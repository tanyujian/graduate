from django.db import models
from user.models import MyUser

# Create your models here.

class CourseVideo(models.Model):
    title=models.CharField(max_length=100)
    cover_url=models.URLField(null=True)
    video_url=models.URLField(null=True)
    cover=models.ImageField(upload_to="image")
    price=models.IntegerField(default=0)
    pub_time=models.DateTimeField(auto_now_add=True)
    teacher=models.ForeignKey(MyUser,on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name="教学视频"
    def __str__(self):
        return self.title
