#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.people.employee import Employee


class ProductOwner(Employee):

    def __init__(self, name: str, salary: int, pizza: str, price: int):
        super().__init__(name, salary)
        self.pizza = pizza
        self.price = price

    def design_pizza(self, shop):
        return shop.add_pizza(self.pizza, self.price)
