from django.urls import path
from .views import TransactionCreateView, TransactionListView, TransactionDetailView, TransactionUpdateView

urlpatterns = [
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:id>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<int:id>/', TransactionUpdateView.as_view(), name='transaction-update'),
]
