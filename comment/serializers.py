from rest_framework import serializers
from .models import Comment
from user.serializers import MyUserSerializers


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=["id"]

class CommentSerializer(serializers.ModelSerializer):
    user=MyUserSerializers()
    reply_user=MyUserSerializers()
    root=ParentSerializer()
    class Meta:
        model=Comment
        fields=["id","content","user","reply_user","pub_time","root"]