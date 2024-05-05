from django.shortcuts import render
from django.contrib import auth
from main.models import Post
from accounts.views import *
# Create your views here.


def mypage(request):
    
    my_blogs = Post.objects.filter(writer=request.user)
    return render(request, 'users/mypage.html',{'my_blogs':my_blogs})
