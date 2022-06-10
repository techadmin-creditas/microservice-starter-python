"""
This is the model for Words
"""
from dataclasses import field
import json

from models.base import base_model, dataclass


@dataclass
class new_word_response(base_model):
    """
    This class represents the New Word Response
    """
    input: str = ""
    message: str = ""
    word_count: int = 0

    def __init__(self, **kwargs) -> None:
        super().__init__()

        self.input = kwargs.get("input", "")
        self.message = kwargs.get("message", "")
        self.word_count = kwargs.get("word_count", 0)


@dataclass
class sql_response_model:
    """
    This class reps the return data from the sql table
    """

    customerInfo: json = field(default_factory=json)
    accountInfo: json = field(default_factory=json)
    balanceInfo: json = field(default_factory=json)
    paymentInfo: json = field(default_factory=json)
    additionalData : json = field(default_factory=json)

    def __init__(self, **kwargs) -> None:
        super().__init__()
        resultset = kwargs.get('kwargs')
        self.customerInfo = {
            'mobileNumber' : resultset.pop("MobileNumber", None),
            'email' : resultset.pop("Email", None),
            'firstName' : resultset.get("FirstName"),
            'lastName' : resultset.get("LastName")
        }
        self.accountInfo = {
            'accountNumber' : resultset.pop("AccountNumber", None),
            'accountType' : resultset.get("APPL")
        }
        self.balanceInfo = {
            'balanceStatus' : resultset.get("Status"),
            'minimumAmountDue' : resultset.get("MinimumAmountDue")
        }
        self.paymentInfo = {
            'lastPaymentAmount' : resultset.get("LastPaymentAmount"),
            'paymentDueDate' : resultset.get("PaymentDueDate")
        }
        self.additionalData = resultset

        
       

