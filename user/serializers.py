from rest_framework import serializers
from .models import MyUser


class MyUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=["id","username","nickname"]