from django import forms
from video.models import CourseVideo
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from django.db.models import ObjectDoesNotExist

class UntilForm(object):
    def get_error_message(self):
        if hasattr(self,"errors"):#判断表单中是否有这个参数
            data=self.errors.get_json_data()
            message = []
            for key,message_error in data.items():
                for message1 in message_error:
                    message.append(message1["message"])
            return message
        else:
            return {}
class CommentForm(forms.Form,UntilForm):
    reply_id=forms.IntegerField()
    object_id=forms.IntegerField()
    content=forms.CharField(widget=forms.Textarea)
    content_type=forms.CharField()
    def clean(self):
        object_id=self.cleaned_data.get("object_id",0)
        content_type=self.cleaned_data.get("content_type","")
        reply_id=self.cleaned_data.get("reply_id")
        try:
            model=ContentType.objects.get(model=content_type).model_class()
            self.cleaned_data["content_object"]=model.objects.get(id=object_id)
        except ObjectDoesNotExist:
            raise forms.ValidationError("没有此课程")
        if not self.cleaned_data.get("content","").strip():
            raise forms.ValidationError("评论不能为空")
        if reply_id<0:
            raise forms.ValidationError("评论出错")
        elif reply_id==0:
            self.cleaned_data["parent"]=None
        else:
            try:
                comment=Comment.objects.get(id=reply_id)
                self.cleaned_data["parent"]=comment
            except ObjectDoesNotExist:
                raise forms.ValidationError("你所回复的评论已不存在")




        