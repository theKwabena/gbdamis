from django.urls import path
from . import views
from .editorview import ckeditor_upload_wrapper, ckeditor_browse_wrapper

urlpatterns = [
    path('forum', views.forum, name='forum'),
    path('posts', views.posts, name = 'posts'),
    path('add-post', views.addNewForumPost, name ='new-post'),
    path('edit-post/<int:id>', views.edit_post, name='edit'),
    path('ckeditor/upload/', ckeditor_upload_wrapper, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_browse_wrapper, name='ckeditor_browse')
]