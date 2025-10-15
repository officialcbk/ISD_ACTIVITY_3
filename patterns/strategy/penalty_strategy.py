"""This module defines the PenaltyStrategy class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

from abc import ABC
from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class PenaltyStrategy(PaymentStrategy):
    def process_payment(self, account:BillingAccount, payee:Payee, amount) -> str:
        """
        Applies a payment and adds a $10.00 penalty.

        Args:
            account (BillingAccount): The billing account..
            payee (Payee): The payee of the account.
            amount (float): The payment amount.

        Returns:
            str: A confirmation message indicating the result of the payment.
        """
       
        account.deduct_balance(payee, amount)

        balance = account.get_balance(payee)

        if balance <= 0:
            return f"Processed payment of ${amount:.2f}. New balance: $0.00."

        account.add_balance(payee, 10.00)
        balance = account.get_balance(payee)

        return f"Insufficient payment. Added penalty fee of $10.00."\
        "New balance: ${balance:.2f}."


      