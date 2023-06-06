from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from .forms import PostForm
# Create your views here.




def ForumPosts(request):

    return render(request, 'forum/addforumpost.html')


def addNewForumPost(request):
    form = PostForm(request.POST or None )
    if form.is_valid():
        pass
    context = {
        'form': form
    }
    return render(request, 'forum/newForumPost.html', context)
