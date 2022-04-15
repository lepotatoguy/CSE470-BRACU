from django.urls import path

# from . import views
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('transaction/<int:pk>', TransactionDetail.as_view(),
         name='transaction_detail'),
    path('transaction-create/', TransactionCreate.as_view(),
         name='transaction-create'),
]
