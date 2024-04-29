from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post

# Create your views here.



def mainpage(request):
    return render(request, 'main/mainpage.html')

def secondpage(request):
    blogs = Post.objects.all()
    return render(request, 'main/secondpage.html', {'blogs': blogs}) 
def new_blog(request):
    return render(request, 'main/new-post.html')

def detail(request, id):
    blog=get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'blog':blog})
def edit(request, id):
    edit_blog = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'blog':edit_blog})


def create(request):
    new_blog = Post()

    new_blog.title = request.POST['title']
    new_blog.stitle = request.POST['stitle']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.image = request.FILES.get('image')

    new_blog.save()

    return redirect('main:detail', new_blog.id)


def update(request,id):
    update_blog = Post.objects.get(pk=id)

    update_blog.title = request.POST['title']
    update_blog.stitle = request.POST['stitle']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.image = request.FILES.get('image')

    update_blog.save()

    return redirect('main:detail', update_blog.id)

def delete(request, id):
    delete_blog= Post.objects.get(pk=id)
    delete_blog.delete()
    return redirect('main:secondpage')

