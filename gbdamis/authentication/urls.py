from django.urls import path

from gbdamis.authentication import views

urlpatterns = [
    path('login', views.login_view, name='login' ),
    path('sign-up', views.sign_up_view, name='signup'),
    path('send', views.send_verification_email, name='send-verification-email'),
    path('verify-email', views.verification_sent, name='verification')
]
