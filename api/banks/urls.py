from django.urls import path

from api.banks import views

urlpatterns = [
    path('banks/', views.banks_api_view)
]
