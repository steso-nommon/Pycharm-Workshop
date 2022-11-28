#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.items.pizza_design import PizzaDesign
from nommon_pizza.people.employee import Employee


class ProductOwner(Employee):

    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)

    def design_pizza(self, pizza_name, ingredients, price):
        return PizzaDesign(pizza_name, ingredients, price)
