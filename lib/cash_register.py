#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        transaction_items = [item for item in self.items if item] 
        num_items = int(self.last_transaction // (self.last_transaction / len(transaction_items)))
        self.items = self.items[:-num_items]
        if self.total < 0:
            self.total = 0.0

    def __repr__(self):
        return f"CashRegister(discount={self.discount}, total={self.total}, items={self.items})"
