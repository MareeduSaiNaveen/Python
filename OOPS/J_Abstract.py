from abc import ABC, abstractmethod         #importing abstract base class module
class A(ABC):
    @abstractmethod
    def f1(self):
        pass
# obj1 = A()                        #cannot create object of abstract class
# obj1.f1()                         #cannot call abstract method

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
        pass
class paypal(PaymentGateway):
    def pay(self):
        print("Payment done using PayPal")
class Razopay(PaymentGateway):
    def pay(self):
        print("Payemnt done using Razopay")
class purchase:
    def __init__(self, gateway):
        self.gateway = gateway
    def checkout(self):
        self.gateway.pay()

p1 = paypal()
order1 = purchase(p1)
order1.checkout()