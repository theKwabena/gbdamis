from django.urls import path
from . import views


urlpatterns = [
    path('member/', views.member_dashboard, name = 'member-dashboard' ),
    path('profile/', views.member_profile, name = 'member-profile' ),
  
]