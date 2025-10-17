"""This module defines the PaymentStrategy class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount
from payee.payee import Payee

class PaymentStrategy(ABC):
    """
    Class for payment strategy
    """
    @abstractmethod
    def process_payment(self, account:BillingAccount, payee:Payee, amount:float) -> str:
        """
        Processes a payment according to the strategy.

        Args:
            account(BillingAccount):The type of account
            payee(Payee): Payee of the account
            amount(float): Amount to be paid

        return: 
           str:Returns a string.
        """
        
        pass

