from django.urls import path

# from . import views
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('', Index.as_view(), name='index'),
    path('transaction/<int:pk>', TransactionDetail.as_view(),
         name='transaction_detail'),
    path('transaction-create/', TransactionCreate.as_view(),
         name='transaction-create'),
    path('transaction-update/<int:pk>', TransactionUpdate.as_view(),
         name='transaction-update'),
    path('transaction-delete/<int:pk>', TransactionDelete.as_view(),
         name='transaction-delete'),
]
