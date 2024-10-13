from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import PaymentProcessor, CreditCardPayment, PayPalPayment
from .forms import PaymentForm
from django.shortcuts import render

def home_view(request):
    return render(request, 'payments/home.html')

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_type = form.cleaned_data['payment_type']
            amount = form.cleaned_data['amount']

            if payment_type == 'credit_card':
                strategy = CreditCardPayment()
            elif payment_type == 'paypal':
                strategy = PayPalPayment()
            else:
                return JsonResponse({'error': 'Invalid payment type'}, status=400)

            processor = PaymentProcessor(strategy)
            result = processor.process(amount)

            return render(request, 'payments/success.html', {'result': result})
    else:
        form = PaymentForm()

    return render(request, 'payments/payment_form.html', {'form': form})

def success_view(request):
    return render(request, 'payments/success.html')
