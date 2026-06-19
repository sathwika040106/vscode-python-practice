from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

p = CreditCard()
p.pay(500)