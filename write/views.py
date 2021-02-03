from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})


def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.email = request.POST['email']
        post.productType = request.POST['productType']
        post.productNum = request.POST['productNum']
        post.bodyText = request.POST['bodyText']
        post.picture = request.FILES['picture']
        post.save()
        return redirect('detail', post.pk)
    return render(request, 'create.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('home')

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.email = request.POST['email']
        post.productType = request.POST['productType']
        post.productNum = request.POST['productNum']
        post.bodyText = request.POST['bodyText']
        post.picture = request.FILES['picture']
        post.save()
        return redirect('detail', post.pk)
    return render(request, 'update.html', {'post':post})