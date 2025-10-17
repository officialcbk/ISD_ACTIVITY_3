"""This module defines the PartialPaymentStrategy class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount  
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class PartialPaymentStrategy(PaymentStrategy):
    def process_payment(self,account:BillingAccount,payee:Payee,amount:float) -> str:
        """
        Process a payment of a partial payment.

        Args:
            account(BillingAccount): Billing account
            payee(Payee): Payee of the account
            amount(float): Amount to be paid

        Return: 
            str:Returns a string.
        """

        account.deduct_balance(payee, amount)

        balance = account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."
        
        return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."
