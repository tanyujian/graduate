from django.shortcuts import render,redirect
from django.http import FileResponse
from django.conf import settings
from django.utils.http import urlquote
from django.contrib.auth.decorators import login_required
from django.db.models import ObjectDoesNotExist
from .models import TechFile,TechWork
from video.models import CourseVideo
# Create your views here.

def tech_condition(request):
    return render(request,"condition.html")

def the_outline(request):
    return render(request,"outline.html")

@login_required(login_url="user:login")
def load_course_file(request,course_id):
    name=TechFile.objects.get(id=course_id)
    file=open(settings.MEDIA_ROOT+name.file.name,"rb")
    response=FileResponse(file)
    response["Content-Type"]="application/octet-stream"
    response["Content-Disposition"]='attachment; filename="%s"'%(urlquote(name.file.name))
    return response

@login_required(login_url="user:login")
def send_work(request):
    file=request.FILES.get("file")
    course_id=request.POST.get("course")
    content={}
    print("===========")
    print(course_id)
    print("===========")
    
    try:
        course = CourseVideo.objects.get(id=course_id)
        if TechWork.objects.filter(user=request.user,course=course).exists():
            tech_work=TechWork.objects.get(user=request.user,course=course)
            tech_work.file=file
            tech_work.save()
        else:
            TechWork(file=file,user=request.user,course=course).save()
    except ObjectDoesNotExist:
        print("cuowu")
    referer = request.META.get("HTTP_REFERER", "/")
    return redirect(referer)