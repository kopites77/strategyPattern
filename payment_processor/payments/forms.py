# payments/forms.py
from django import forms

class PaymentForm(forms.Form):
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
    ]
    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES, label='Payment Method')
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Amount')
