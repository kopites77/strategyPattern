from django.urls import path
from .views import payment_view, payment_details_view, confirmation_view

urlpatterns = [
    path('', payment_view, name='payment_form'),
    path('details/', payment_details_view, name='payment_details'),
    path('confirmation/', confirmation_view, name='payment_confirmation'),
]
