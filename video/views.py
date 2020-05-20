from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CourseVideo
from django.contrib.contenttypes.models import ContentType
from comment.models import Comment
from django.http import Http404,JsonResponse
from django.conf import settings
import time,hmac,os,hashlib
from until.until import get_classify
from tech_assist.models import TechFile
# Create your views here.


def introduce_views(request):
    return render(request,"course_introduce.html")

def course_video(request):
    video=CourseVideo.objects.all()
    content=get_classify(request,video)
    return render(request,"video/main.html",content)

@login_required(login_url="user:login")
def course_detail(request,video_id):
    content={}
    try:
        video=CourseVideo.objects.get(id=video_id)
        content["content"]=video
        content_type=ContentType.objects.get_for_model(content["content"])
        object_id=content["content"].id
        content["comment"]=Comment.objects.filter(content_type=content_type,object_id=object_id,parent=None)
        content["ware"]=TechFile.objects.filter(video=video)
    except:
        raise Http404
    return render(request,"video/video_detail.html",content)

#百度点播获取token
def video_token(request):
    file = request.GET.get('video')

    # course_id = request.GET.get('course_id')
    # if not CourseOrder.objects.filter(course_id=course_id, buyer=request.user, status=2).exists():
    #     return restful.params_error(message='请先购买课程！')

    expiration_time = int(time.time()) + 2 * 60 * 60

    user_id = settings.USER_ID
    user_key = settings.USER_KEY
    print(file)
    # file=http://hemvpc6ui1kef2g0dd2.exp.bcevod.com/mda-igjsr8g7z7zqwnav/mda-igjsr8g7z7zqwnav.m3u8
    extension = os.path.splitext(file)[1]
    media_id = file.split('/')[-1].replace(extension, '')
    print(media_id)
    # unicode->bytes=unicode.encode('utf-8')bytes
    key = user_key.encode('utf-8')
    message = '/{0}/{1}'.format(media_id, expiration_time).encode('utf-8')
    signature = hmac.new(key, message, digestmod=hashlib.sha256).hexdigest()
    token = '{0}_{1}_{2}'.format(signature, user_id, expiration_time)
    return JsonResponse({"code":200,"data":token})

