# Abstraction in Python is an OOP concept that hides unnecessary implementation details from the user, exposing only the essential functionalities. 
# It allows developers to focus on what a component does rather than how it does it. 
# Abstraction is achieved using abstract classes and abstract methods defined in the built-in abc module

# Key Concepts
# Abstract Class: A blueprint for other classes that cannot be instantiated directly.
# Abstract Method: A method declared in an abstract class but without an implementation. Subclasses are required to provide the implementation for these methods, enforcing a consistent interface.
# abc module: Provides the infrastructure for defining Abstract Base Classes (ABCs) in Python.
# @abstractmethod decorator: Marks a method as abstract

# This example demonstrates how an abstract base class PaymentMethod defines a common interface for different payment types like CreditCardPayment and PayPalPayment, 
# while hiding the specific processing logic. 


from abc import ABC, abstractmethod

# Define the abstract base class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Abstract method to process a payment. Must be implemented by subclasses."""
        pass
    
    def display_message(self):
        """Concrete method (with implementation) that all subclasses can use."""
        print("Processing payment...")

# Define a concrete subclass for credit cards
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        # Specific implementation details are hidden from the main program logic
        print(f"Authorizing and processing credit card payment of ${amount}.")
        # ... internal complex logic for credit card processing ...

# Define a concrete subclass for PayPal
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        # Specific implementation details for PayPal
        print(f"Logging into PayPal and processing payment of ${amount}.")
        # ... internal complex logic for PayPal processing ...

# Usage
card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

card_payment.display_message()
card_payment.process_payment(100)

paypal_payment.display_message()
paypal_payment.process_payment(50)

# Attempting to instantiate the abstract class directly will raise a TypeError
try:
    generic_payment = PaymentMethod()
except TypeError as e:
    print(f"\nError: {e}")
