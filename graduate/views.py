from django.shortcuts import render
from video.models import CourseVideo

def index(request):
    course=CourseVideo.objects.all().order_by("-pub_time")[:5]
    content={"course":course}
    return render(request,"index.html",content)