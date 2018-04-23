from db.repository import CashMachineDB, MoneySlipsDB, BankAccountDB


class CashMachineInsertMoneyBill:

    @staticmethod
    def insert_money_bill(money_bill, amount):
        cash_machine = CashMachineDB.get()
        cash_machine.money_slips[money_bill] += amount
        MoneySlipsDB.update(cash_machine)
        return cash_machine


class CashMachineWithDraw:

    @staticmethod
    def withdraw(bank_account, value):
        cash_machine = CashMachineDB.get()
        money_slips_user = cash_machine.withdraw(value)
        if money_slips_user:
            CashMachineWithDraw.__balance_debit(bank_account, value)
            MoneySlipsDB.update(cash_machine)
        return cash_machine

    @staticmethod
    def __balance_debit(bank_account, value):
        bank_account.balance_debit(value)
        BankAccountDB.update_value(bank_account)
