#!/usr/bin/env python3

class CashRegister:
    
    def  __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_item = []

    @property
    def discount(self):
        return self._discount
    
    @discount.setter
    def discount(self, discount):
        self._discount = discount

    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self, total):
        self._total = total

    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, items):
        self._items = items

    @property
    def last_item(self):
        return self._last_item
    
    @last_item.setter
    def last_item(self, last_item):
        self._last_item = last_item

    def add_item(self, title, price, quantity = 1):
        self._last_item.clear()
        self._last_item.append(price)
        self._last_item.append(quantity)
        self._total += price * quantity
        if quantity > 1 :
            a = 0
            while a < quantity:
                self._items.append(title)
                a += 1
        else:
            self._items.append(title)        

    def apply_discount(self):
        if self._discount != 0:
            self._total = self._total - self._total * self._discount / 100
            print(f"After the discount, the total comes to ${self._total:.0f}.")
        else:
            print("There is no discount to apply.")


    def void_last_transaction(self):
        if self._last_item[1] > 1  and len(self._items) > self._last_item[1]:
            b = self._last_item[1]
            while b > 0 :
                self._total = self._total - self._last_item[0]
                self._items.pop()
                b -= 1
        elif self._last_item[1] == 1 and len(self._items) > 1:
            self._total = self._total - self._last_item[0]
        else:
            self._total = 0.0
