from django.urls import path

from . import views

urlpatterns = [
    path('', views.celery_task, name='cel_task'),
    path('schedule/', views.schedule_task, name='schedule')
]
