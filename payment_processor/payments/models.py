from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount:.2f}")

class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.process_payment(amount)
