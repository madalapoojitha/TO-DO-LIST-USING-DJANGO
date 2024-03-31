from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('remove/<int:task_id>/', views.remove_task, name='remove_task'),
    path('completed/<int:task_id>/', views.mark_as_completed, name='mark_as_completed'),
]
