from django.urls import path
from . import views


urlpatterns = [
    path('member/', views.member_dashboard, name = 'member-dashboard' ),
    path('profile/', views.member_profile, name = 'member-profile' ),
    path('dues/', views.dues, name='member-dues'),
    path('executvies', views.executives, name='member-executives')
  
]