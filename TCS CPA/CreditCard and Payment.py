# Author : Nanthakumar J J

# Profile : jjnanthakumar.github.io

__author__ = "https://jjnanthakumar.github.io"

from datetime import datetime


class CreditCard:
    def __init__(self, card_number, card_holder, bank_name, expiry_date, balance, credit_limit):
        self.card_number = card_number
        self.card_holder = card_holder
        self.bank_name = bank_name
        self.expiry_date = expiry_date
        self.balance = balance
        self.credit_limit = credit_limit


def pay(credit_cards, amount, payment_date):
    card = max(credit_cards, key=lambda x: (x.credit_limit-x.balance))
    exp_date = datetime.strptime(card.expiry_date, '%d-%m-%Y')
    not_expired_yet = payment_date <= exp_date
    not_exceeded_limit = amount <= card.credit_limit
    if not_expired_yet and not_exceeded_limit:
        card.balance += amount
        return card


if __name__ == "__main__":
    N = int(input())
    credit_cards = [CreditCard(input(), input(), input(), input(), int(
        input()), int(input())) for _ in range(N)]
    payment_amt = int(input())
    payment_date = datetime.strptime(input(), '%d-%m-%Y')
    card = pay(credit_cards, payment_amt, payment_date)
    if card is None:
        print("Payment not completed.")
    else:
        print("Card details after payment:")
        print(f'{card.card_number}, {(card.credit_limit-card.balance)}, {card.balance}')
