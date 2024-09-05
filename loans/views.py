from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Customer,Loan,Payment
from .serializers import CustomerSerializer,LoanSerializer,PaymentSerializer
from django.shortcuts import get_object_or_404

from decimal import Decimal

class CustomerListCreateView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    
class LoanIssueView(APIView):
    def post(self, request):
        customer_id=request.data.get('customer_id')
        loan_amount=float(request.data.get('princial_amount'))
        loan_period=int(request.data.get('loan_period'))
        interest_rate=float(request.data.get('interest_rate'))
        
        
        #calculation
        interest=loan_amount*loan_period*(interest_rate/100)
        total_amount=loan_amount + interest
        monthly_emi = round(total_amount / (loan_period * 12),2)
        
        
        customer = get_object_or_404(Customer, id=customer_id)
        
        loan_data = {
            'customer': customer.id,
            'princial_amount': loan_amount,
            'interest_rate': interest_rate,
            'loan_period': loan_period,
            'total_amount': total_amount,
            'monthly_emi': monthly_emi,
            'emi_left': loan_period * 12
        }
        
        
        
        loan_serializer = LoanSerializer(data=loan_data)
        if loan_serializer.is_valid():
            loan_serializer.save()
            return Response(loan_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(loan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class LoanPaymentView(APIView):
    def post(self, request):
        loan_id=request.data.get('loan_id')
        payment_amount=float(request.data.get('payment_amount'))
        payment_type=request.data.get('payment_type')
        
        loan = get_object_or_404(Loan, id=loan_id)
        
#        if payment_amount > loan.monthly_emi:
#            return Response({'error': 'Payment amount exceeds monthly EMI'}, status=status.HTTP_400_BAD_REQUEST)
        
        loan.emi_left -= 1
        loan.amount_paid +=Decimal(payment_amount)
     #   loan.total_amount -= Decimal(payment_amount)
        
        
        loan.save()
        
        payment_data = {
            'loan': loan.id,
            'payment_amount': payment_amount,
            'payment_date': request.data.get('payment_date'),
            'payment_type': payment_type
        }
        
        payment_serializer = PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return Response(payment_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LedgerView(APIView):
    def get(self, request,loan_id):
        loan=get_object_or_404(Loan,id=loan_id)
        
        # payments=Payment.objects.filter(loan=loan).order_by('-id')
        serializer = LoanSerializer(loan)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
        # loan_data={
        #     "transactions": payments,
        #     "balance_amount": loan.total_amount - loan.amount_paid,
        #     "monthly_emi": loan.monthly_emi,
        #     "emi_left": loan.emi_left
        # }
        
        # serializer=PaymentSerializer(data=loan_data)
        # return Response(data=serializer.data)
    
    
        # return Response({
        #     "transactions": payments,
        #     "balance_amount": loan.total_amount - loan.amount_paid,
        #     "monthly_emi": loan.monthly_emi,
        #     "emi_left": loan.emi_left
        # }, status=status.HTTP_200_OK)
        