from django.urls import path

from api import views

urlpatterns = [
    path('banks/', views.BankListAPIView.as_view(), name='banks_api'),
    path('bank/create/', views.CreateBankAPIView.as_view(), name='create_bank_api'),
    path('user-token/', views.TokenObtainAPIView.as_view(), name='user_token_api'),
    path('accounts/', views.AccountListCreateAPIView.as_view(), name='account_list_create_api'),
    path('account/<int:pk>/', views.AccountRetrieveUpdateDestroyAPIView.as_view(),
         name='account_retrieve_update_delete_api'),
]
