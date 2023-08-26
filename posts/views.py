from django.shortcuts import render
from .models import Post


def post_list (request):
    data = Post.objects.all()
    return render(request,'all_posts.html',{})


def post_detail(request):
    pass
