from django.shortcuts import render
from .models import Post


def post_list (repuest):
    data = Post.objects.all()
    return render(repuest,'all_posts.html',{})


def post_detail(repuest):
    pass
