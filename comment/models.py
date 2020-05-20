from django.db import models
from user.models import MyUser
from video.models import CourseVideo
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.

class Comment(models.Model):
    content=models.TextField()
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    parent=models.ForeignKey("self",on_delete=models.DO_NOTHING,related_name="comment_parent",null=True)
    root=models.ForeignKey("self",on_delete=models.DO_NOTHING,related_name="comment_root",null=True)
    reply_user=models.ForeignKey(MyUser,on_delete=models.DO_NOTHING,related_name="reply",null=True)
    pub_time=models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    class Meta:
        ordering=("-pub_time",)


