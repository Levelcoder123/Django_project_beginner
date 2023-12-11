from django.urls import path

from api import views

urlpatterns = [
    path('banks/', views.BankListAPIView.as_view(), name='banks_api'),
    path('user-token/', views.CreateUserTokenAPIView.as_view(), name='user_token_api'),
    path('accounts/', views.AuthorizedUserAccountsAPIView.as_view(), name='user-accounts_api'),
]
