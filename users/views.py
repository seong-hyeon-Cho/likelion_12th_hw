from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from main.models import Post
from accounts.views import *

# Create your views here.


def mypage(request, id):
    user=get_object_or_404(User, pk=id)
    my_blogs=Post.objects.filter(writer=user)

    # 추가: 팔로잉, 팔로워 리스트 가져오기
    following_list = user.profile.followings.all()
    follower_list = user.profile.followers.all()


    context ={
        'user':user,
        'my_blogs':my_blogs,
        'following_list': following_list,  # 팔로잉 리스트
        'follower_list': follower_list,    # 팔로워 리스트
    }
    return render(request, 'users/mypage.html', context)
    ## my_blogs = Post.objects.filter(writer=request.user)
    ## return render(request, 'users/mypage.html',{'my_blogs':my_blogs})

def follow(request, id):
    user= request.user
    followed_user=get_object_or_404(User, pk=id)
    is_follower=user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)