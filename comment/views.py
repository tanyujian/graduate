from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import CommentForm
from .models import Comment
from until.until import Until
from .serializers import CommentSerializer
# Create your views here.


def comment(request):
    form=CommentForm(request.POST)
    until=Until()
    if form.is_valid():
        content=form.cleaned_data.get("content","")
        reply_id=form.cleaned_data.get("reply_id",0)
        parent=form.cleaned_data["parent"]
        comment_=Comment()
        comment_.content_object=form.cleaned_data.get("content_object")
        comment_.content=content
        comment_.user=request.user
        if parent is None:
            comment_.parent=None
        else:
            comment_.parent=parent
            comment_.reply_user=parent.user
            comment_.root=parent.root if not parent.root is None else parent
        comment_.save()
        data=CommentSerializer(comment_).data
        return until.ok(data=data)
    else:
        return until.form_error(data=form.get_error_message())