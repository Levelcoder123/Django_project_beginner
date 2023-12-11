from django.urls import path

from . import views

urlpatterns = [
    path('', views.BankListView.as_view(), name='banks')
]
