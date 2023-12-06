from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.get_accounts_data)
]
