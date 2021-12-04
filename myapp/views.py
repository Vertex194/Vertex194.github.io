import datetime
from django import template
from django.shortcuts import redirect, render
# Create your views here.
from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import Post
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.datetime.now()
    html = template.render(locals())
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")
    # return HttpResponse(post_lists)
    return render(request,'index.html',locals())
def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post !=None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
# def index(request):
#     return HttpResponse("My First Django App.")
# def homepage(request):
#     now = datetime.datetime.now() #現在時間
#     context ={'now':now}
#     return render(request,'homepage.html',context)
# def show(request):
#     #render的必要參數有：
#     # ✦ request
#     # ✦ template_name：要使用的網頁模版。
#     # 另外這個範例還加了一個非必要參數：
#     # ✦ context：必須是dictionary。
#     return render(request,'hello_django.html',{
#         'data':"Hello Django"
#     })