"""This module defines the Payment class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class Payment:
    def __init__(self, strategy: PaymentStrategy):
        """
        Initializes a Payment strategy.

        Args:
            strategy (PaymentStrategy): The strategy to be used for processing payments.

        Raises:
            ValueError: If the strategy provided is not a valid PaymentStrategy instance.
        """

        if isinstance(strategy, PaymentStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Invalid Strategy")

    def pay_bill(self, account:BillingAccount, payee:Payee, amount: float) -> str:
        """
        Implements the payment using the assigned strategy.

        Args:
            account (BillingAccount): The billing account to apply the payment to.
            payee (Payee): The payee receiving the payment.
            amount (float): The amount to be paid.

        Returns:
            str: The confirmation message from the applied strategy.
        """
        return self.strategy.process_payment(account, payee, amount)
