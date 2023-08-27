from django.shortcuts import render
from .models import Post


def post_list (request):
    data = Post.objects.all()
    return render(request,'all_posts.html',{'posts':data})


def post_detail(request,post_id):
    data = Post.objects.git(id=post_id)
    return render(request,'post_detail.html',{'post':data})
