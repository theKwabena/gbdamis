from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard' ),

    #Members
    path('members', views.members, name='members'),
    path('add-member/', views.add_member, name='add-member'),
    path('g-us', views.generate_username, name ='generate-username'),

    #news, announcements, events
    path('news', views.news, name = 'news'),
    path('announcements', views.announcements, name = 'announcements'),
    path('add-annoucement', views.add_announcements, name = 'add-annoucement'),
    path('events', views.events, name='events'),

    #Voting and Elections
    path('nominations/', views.nominations, name='admin-nominations'),
]