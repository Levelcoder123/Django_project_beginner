from django.urls import path

from api.banks import views

urlpatterns = [
    path('banks/', views.BanksApiView.as_view(), name='banks')
]
