import logging
from django.shortcuts import render, redirect, get_object_or_404
# import JsonResponse
from django.http import JsonResponse
from django.http import HttpResponseForbidden
# Create your views here.
from django.shortcuts import render
from django_select2.views import AutoResponseView


from .forms import PostForm

from gbdamis.forum.models import Post

# Create your views here.
log = logging.getLogger(__name__)



class TagAutoResponseView(AutoResponseView):
    def get(self, request, *args, **kwargs):
        """
        This method is overriden for changing id to name instead of pk.
        """
        self.widget = self.get_widget_or_404()
        self.term = kwargs.get('term', request.GET.get('term', ''))
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return JsonResponse({
            'results': [
                {
                    'text': self.widget.label_from_instance(obj),
                    'id': obj.name,
                }
                for obj in context['object_list']
                ],
            'more': context['page_obj'].has_next()
        })

def forum(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    
    return render(request, 'forum/members-forum.html', context)



def addNewForumPost(request):
    form = PostForm(request.POST or None, request.FILES or None)
    log.warning(form['tag'].value())
    log.warning(request.POST.get('tag'))
    log.warning(request.POST.get('featured_image'))
    if form.is_valid():
        log.info(form.cleaned_data.get('tag'))
        log.info(form.cleaned_data)
               # post = form.save(commit=False)
        # post.author = request.user
        # post.save()

        return redirect('posts')

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
    
    form = PostForm(request.POST or None, request.FILES or None, instance= post)
    
    if form.is_valid():
        log.info(form.cleaned_data)
        # form.save()
        # return redirect('posts')
    context = {
        'form' : form,
        'edit': True
    }

    return render(request, 'forum/newForumPost.html', context)



