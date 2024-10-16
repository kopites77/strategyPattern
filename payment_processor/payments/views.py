from django.shortcuts import render, redirect
from .models import PaymentProcessor, CreditCardPayment, PayPalPayment
from .forms import PaymentForm

def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            request.session['payment_type'] = form.cleaned_data['payment_type']
            request.session['amount'] = float(form.cleaned_data['amount'])

            return redirect('payment_details')

    else:
        form = PaymentForm()

    return render(request, 'payments/payment_form.html', {'form': form})

def payment_details_view(request):
    payment_type = request.session.get('payment_type')
    amount = request.session.get('amount', 0)

    if request.method == 'POST':
        if payment_type == 'credit_card':
            strategy = CreditCardPayment()
        elif payment_type == 'paypal':
            strategy = PayPalPayment()

        processor = PaymentProcessor(strategy)
        result = processor.process(amount)

        print(f"Payment Result: {result}")  

        request.session['payment_result'] = result

        return redirect('payment_confirmation')

    template = 'payments/credit_card_form.html' if payment_type == 'credit_card' else 'payments/paypal_form.html'
    return render(request, template)



def confirmation_view(request):
    result = request.session.get('payment_result', 'No result available.')

    print(f"Confirmation Result: {result}")

    return render(request, 'payments/confirmation.html', {'result': result})


