from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.admin_dashboard, name='admin-dashboard' ),

    #Members
    path('members', views.members, name='members'),
    path('add-member/', views.add_member, name='add-member'),
    path('members/<int:id>/approve', views.approve_member, name='approve_member'),
    path('members/<int:id>/decline', views.decline_member, name='approve_member'),
    path('g-us', views.generate_username, name ='generate-username'),
    path('check-email', views.check_email, name='check_email'),
    path('check_phone', views.check_phone_number, name='check_phone_number'),
    path('remove-member/<int:id>', views.remove_member, name='remove-member'),
    path('check-password', views.check_password, name='check_password'),
    path('edit-member/<int:id>', views.edit_member, name='edit-member'),
    path('member/<int:id>/make-admin', views.make_admin, name='make-admin'),
    path('member/<int:id>/remove-admin', views.remove_admin, name ='remove-admin'),

    #news, announcements, events
    path('news', views.news, name = 'news'),
    path('news/<int:id>', views.news_item, name='news'),
    path('announcements', views.announcements, name = 'announcements'),
    path('announcement/<int:id>', views.announcement, name='announcement'),
    path('announcement/<int:id>/edit', views.edit_announcement, name='delete'),
    path('add-annoucement', views.add_announcements, name = 'add-annoucement'),
    path('events', views.events, name='events'),

    #Voting and Elections
    path('nominations/', views.nominations, name='admin-nominations'),
]