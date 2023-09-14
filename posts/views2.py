from .models import Post
from django.views import generic



class PostList(generic.ListView):
    model = Post