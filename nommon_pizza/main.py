#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.items.pizza import Pizza
from nommon_pizza.shop.shop import Shop

if __name__ == '__main__':
    shop = Shop.create_shop()

    # Exercise 1: Create a pizza
    shop.product_owner.design_pizza(shop)
    pizza = shop.employees["Pepe"].create_pizza(shop.pizzas["Hawaiana"], "hot")
    print(pizza)
