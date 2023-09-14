from .models import Post
from django.views import generic



class PostList(generic.ListView):
    model = Post



class PostDetail(generic.DetailView):
    model = Post
    success_url= '/blog/'



class PostCreate(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url= '/blog/'


class PostUpdet(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url= '/blog/'
    template_name='posts/edit_post.html'


class PostDelete(generic.DeleteView):
    model = Post
