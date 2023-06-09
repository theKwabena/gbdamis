import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
# Create your views here.
from django.shortcuts import render


from .forms import PostForm
from . models import Post
# Create your views here.
log = logging.getLogger(__name__)

def forum(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    
    return render(request, 'forum/members-forum.html', context)



def addNewForumPost(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('posts')
    else:
        form = PostForm()
    context = {
        'form': form,
        
    }
    return render(request, 'forum/newForumPost.html', context)


def posts(request):
    posts = Post.objects.filter(author=request.user)

    context = {
        'posts' : posts
    }

    return render(request, 'forum/user-posts.html', context)


def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if post.author != request.user:
        return HttpResponseForbidden('Not Authorized')
    
    form = PostForm(request.POST or None, instance= post)

    if form.is_valid():
        form.save()
        return redirect('posts')
    context = {
        'form' : form,
        'edit': True
    }

    return render(request, 'forum/newForumPost.html', context)
