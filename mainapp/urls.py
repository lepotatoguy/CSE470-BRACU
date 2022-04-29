from django.urls import path

# from . import views
from .views import *

from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('', Index.as_view(), name='index'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile-create/', ProfileCreate.as_view(),
         name='profile-create'),
    path('transaction/<int:pk>', TransactionDetail.as_view(),
         name='transaction_detail'),
    path('transaction-create/', TransactionCreate.as_view(),
         name='transaction-create'),
    path('transaction-update/<int:pk>', TransactionUpdate.as_view(),
         name='transaction-update'),
    path('transaction-delete/<int:pk>', TransactionDelete.as_view(),
         name='transaction-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
