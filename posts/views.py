from django.shortcuts import render
from .models import Post


def post_list (repuest):
    data = Post.objects.all()


def post_detail(repuest):
    pass
