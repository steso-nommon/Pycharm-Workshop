#!/usr/bin/python3

"""
 Module description: pizza
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.items.pizza import Pizza
from nommon_pizza.shop.shop import Shop

if __name__ == '__main__':
    shop = Shop.create_shop()

    # Exercise 1: Create a pizza
    pizza_design = shop.product_owner.design_pizza("Hawaiana", ["piña"], 10)
    shop.add_pizza_design(pizza_design)
    pizza = shop.employees["Pepe"].create_pizza(shop.pizza_designs["Hawaiana"], Pizza.PIZZA_STATUS_HOT)
    print(pizza)
