from db.repository import BankAccountDB
from db.models import BankAccount, Agency
from exceptions import AppException
from typing import Optional

class AuthBankAccount:
    bank_account_authenticated: BankAccount = None

    @staticmethod
    def authenticate(agency_number, account_number, password) -> Optional[BankAccount]:
        bank_account_to_find = BankAccount(
            number=account_number,
            password=password,
            agency=Agency(number=agency_number)
        )
        try:
            bank_account = AuthBankAccount.__find_bank_account(bank_account_to_find)
            AuthBankAccount.bank_account_authenticated = bank_account
            return bank_account
        except AppException:
            # raise err
            return None

    @staticmethod
    def __find_bank_account(bank_account: BankAccount):
        return BankAccountDB.find_by_number_and_password_and_agency_number(bank_account)
