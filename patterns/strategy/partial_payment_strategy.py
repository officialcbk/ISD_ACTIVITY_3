"""This module defines the PartialPaymentStrategy class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from billing_account.billing_account import BillingAccount  
from payee.payee import Payee
from patterns.strategy.payment_strategy import PaymentStrategy

class PartialPaymentStrategy(PaymentStrategy):
