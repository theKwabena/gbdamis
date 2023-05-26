from django.urls import path
from . import views
urlpatterns = [
    path('position/<int:pk>/', views.delete_position, name='delete-position'),
    path('nomination/<int:pk>/', views.delete_nomination, name='delete-nomination')
]
