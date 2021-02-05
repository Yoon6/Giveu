from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})


def create(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.email = request.user
            instance.save()
            return redirect('detail', post_id = instance.pk)
    else:
        form = PostForm()
    return render(request, 'create.html', {'form':form})

def detail(request, post_id):
    if not request.user.is_authenticated: # 로그인을 안했으면 글 못읽게
        return redirect('home')
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def delete(request, post_id):

    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home')

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'update.html', {'form':form})