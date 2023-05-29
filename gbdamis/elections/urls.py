from django.urls import path
from . import views
urlpatterns = [
    path('position/<int:pk>/delete', views.delete_position, name='delete-position'),
    path('nomination/<int:pk>/delete', views.delete_nomination, name='delete-nomination'),
    path('nominations/<int:pk>/approve', views.approve_nomination, name='approve-nomination'),
    path('nominations/<int:pk>/decline', views.decline_nomination, name='decline-nomination')
]
