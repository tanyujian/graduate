from django.http import JsonResponse
from django.core.paginator import Paginator

class Until(object):
    data={}
    def ok(self,message="",data=None):
        self.data["code"]=200
        self.data["message"]=message
        self.data["data"]=data
        return JsonResponse(self.data)

    def error(self,message="",data=None):
        self.data["code"]=404
        self.data["message"]=message
        self.data["data"]=data
        return JsonResponse(self.data)
    def form_error(self,message="",data=None):
        self.data["code"]=405
        self.data["message"]=message
        self.data["data"]=data
        return JsonResponse(self.data)


def get_classify(request,blog_data):
    content = {}
    blog_num = request.GET.get("page",1)  # 得到当前页的网址
    paginator = Paginator(blog_data, 8)  # 对数据进行分页
    num = paginator.get_page(blog_num)  # 对当前页分配内容
    blog_page = list(range(max(num.number - 2, 1), min(num.number + 2, paginator.num_pages + 1)))
    if blog_page[0] - 2 - 1 >= 0:
        blog_page.insert(0, "...")
    if paginator.num_pages - num.number - 2 > 0:
        blog_page.append("...")
    if blog_page[0] != 1:
        blog_page.insert(0, 1)
    if blog_page[-1] != paginator.num_pages:
        blog_page.append(paginator.num_pages)
    content["num"] = num
    content["blog_page"] = blog_page
    return content





