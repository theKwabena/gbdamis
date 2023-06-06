from django.urls import path
from . import views

urlpatterns = [
    path('add-post', views.addNewForumPost, name ='new-forum-post')
]