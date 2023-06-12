from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_view, name='login' ),
    path('sign-up', views.sign_up_view, name='signup'),
    path('verify-email', views.verification_sent, name='verification')
]
