from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Loan(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    princial_amount=models.DecimalField(max_digits=10,decimal_places=2)
    interest_rate=models.DecimalField(max_digits=5,decimal_places=2)
    loan_period=models.IntegerField()
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    monthly_emi=models.DecimalField(max_digits=10,decimal_places=2)
    amount_paid=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    emi_left=models.IntegerField(default=0)
    
    def __str__self(self):
        return f'Loan no - {self.id} {self.customer.name}'
    
class Payment(models.Model):
    payment_type_choices=[
        ('EMI','EMI'),
        ('FULL PAYMENT','FULL PAYMENT'),
    ]
    
    loan=models.ForeignKey(Loan,on_delete=models.CASCADE)
    payment_amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_date=models.DateTimeField(default=timezone.now)
    payment_type=models.CharField(max_length=25,choices=payment_type_choices)
    
    def __str__(self):
        return f'Receipt no - {self.id} {self.loan.customer.name}'
    
    
    