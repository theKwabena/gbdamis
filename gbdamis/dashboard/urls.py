from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='dashboard' ),

    #Members
    path('members', views.members, name='members'),
    path('add-member/', views.add_member, name='add-member'),
    path('g-us', views.generate_username, name ='generate-username'),
    path('check-email', views.check_email, name='check_email'),
    path('check_phone', views.check_phone_number, name='check_phone_number'),
    path('remove-member/<int:id>', views.remove_member, name='remove-member'),

    #news, announcements, events
    path('news', views.news, name = 'news'),
    path('announcements', views.announcements, name = 'announcements'),
    path('add-annoucement', views.add_announcements, name = 'add-annoucement'),
    path('events', views.events, name='events'),

    #Voting and Elections
    path('nominations/', views.nominations, name='admin-nominations'),
]