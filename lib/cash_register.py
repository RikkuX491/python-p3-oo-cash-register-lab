#!/usr/bin/env python3

class CashRegister:
    
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity = 1):
        self.total += (price * quantity)

        for i in range(quantity):
          self.items.append(title)

        # self.last_transaction = price * quantity

        self.last_transaction = {
           "price": price,
           "quantity": quantity
        }

    def apply_discount(self):
        if(self.discount > 0):
          self.total -= (self.total * (self.discount / 100))

          print(f"After the discount, the total comes to ${int(self.total)}.")

        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
       #  self.total -= self.last_transaction
       self.total -= (self.last_transaction['price'] * self.last_transaction['quantity'])
       
       for i in range(self.last_transaction['quantity']):
          self.items.pop()