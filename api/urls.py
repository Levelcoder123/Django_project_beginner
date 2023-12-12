from django.urls import path

from api import views

urlpatterns = [
    path('banks/', views.BankListAPIView.as_view(), name='banks_api'),
    path('bank/create/', views.CreateBankAPIView.as_view(), name='create_bank_api'),
    path('user-token/', views.TokenObtainAPIView.as_view(), name='user_token_api'),
    path('accounts/', views.AccountListAPIView.as_view(), name='user_accounts_api'),
    path('account/create/', views.CreateAccountAPIView.as_view(), name='create_account_api'),
    path('account/update/<int:number>/', views.UpdateAccountAPIView.as_view(), name='update_account_api'),
    path('account/delete/<int:number>/', views.DeleteAccountAPIView.as_view(), name='delete_account_api'),
    path('account/detail/', views.AccountDetailAPIView.as_view(), name='account_detail_api'),
]
