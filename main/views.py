from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post,Comment,Tag

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
    if request.method == 'GET':
        comments=Comment.objects.filter(blog=blog)
        return render(request, 'main/detail.html',{'blog':blog, 'comments':comments})
    elif request.method=='POST':
        new_comment = Comment()
        new_comment.blog=blog
        new_comment.writer=request.user
        new_comment.content=request.POST['content']
        new_comment.pub_date = timezone.now()

        new_comment.save()
        return redirect('main:detail',id)

    


def edit(request, id):
    edit_blog = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'blog':edit_blog})


def create(request):
    if request.user.is_authenticated:
        new_blog = Post()

        new_blog.title = request.POST['title']
        new_blog.stitle = request.POST['stitle']
        new_blog.writer = request.user
        new_blog.body = request.POST['body']
        new_blog.pub_date = timezone.now()
        new_blog.image = request.FILES.get('image')

        new_blog.save()

        words=new_blog.body.split(' ')
        tag_list=[]

        for w in words:
            if len(w)>0:
                if w[0]=='#':
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean=Tag.objects.get_or_create(name=t)
            new_blog.tags.add(tag.id)

        return redirect('main:detail', new_blog.id)
    else:
        return redirect('accounts:login')


def update(request,id):
    update_blog = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_blog.writer:
        update_blog.title = request.POST['title']
        update_blog.stitle = request.POST['stitle']
        update_blog.body = request.POST['body']
        update_blog.pub_date = timezone.now()
        
        if request.FILES.get('image'):
            update_blog.image = request.FILES.get('image')

        update_blog.save()
        return redirect('main:detail', update_blog.id)
    return redirect('accounts:login', update_blog.id)

def delete(request, id):
    delete_blog= Post.objects.get(pk=id)
    delete_blog.delete()
    return redirect('main:secondpage')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user == comment.writer:
        comment.delete()
    return redirect('main:detail', id=comment.blog.id)

def tag_list(request):
    tags=Tag.objects.all()
    return render(request, 'main/tag-list.html', {'tags':tags })

def tag_blogs(request, tag_id):
    tag= get_object_or_404(Tag,id =tag_id)
    blogs=tag.blogs.all()
    return render(request,'main/tag-blog.html',{
        'tag':tag,
        'blogs':blogs
    })
