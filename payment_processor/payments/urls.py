from django.urls import path
from .views import payment_view, success_view

urlpatterns = [
    path('', payment_view, name='payment_form'),
    path('success/', success_view, name='payment_success'),
]
