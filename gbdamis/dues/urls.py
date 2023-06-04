from django.urls import path
from . import views
urlpatterns = [
    path('pay-dues/', views.pay_dues, name='pay_dues')
]
