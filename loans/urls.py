from django.urls import path
from .views import CustomerListCreateView, CustomerRetrieveUpdateDestroyView,LoanIssueView,LoanPaymentView,LedgerView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-retrieve-update-destroy'),
    path('issue/', LoanIssueView.as_view(), name='loan_issue'),
    path('payment/', LoanPaymentView.as_view(), name='loan_payment'),
    path('ledger/<int:loan_id>/', LedgerView.as_view(), name='ledger'),
]