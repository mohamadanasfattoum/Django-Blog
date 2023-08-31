from django.shortcuts import render , redirect
from .models import Post, Comment
from .forms import PostForm

def post_list (request):
    data = Post.objects.all()
    return render(request,'all_posts.html',{'posts':data})


def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    comment_data = Comment.objects.all()
    return render(request,'post_detail.html',{'post':data , 'comment':comment_data})



def add_post(request):
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/')
    else:
        form = PostForm()
    return render(request,'add_post.html',{'form':form})



def edit_post(request,post_id):
    data = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect(f'/blog/{data.id}')

    else:
        form = PostForm(instance=data)

    return render(request,'edit_post.html',{'form':form})


def delete_post(request,post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog/')