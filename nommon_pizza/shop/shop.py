#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.employees.employee import Employee
from nommon_pizza.employees.product_owner import ProductOwner


class Shop:

    def __init__(self, employees, product_owner):
        self.employees = employees
        self.product_owner = product_owner
        self.pizzas = dict()

    @staticmethod
    def create_shop():
        pepe = Employee("Pepe", 20000)
        juana = Employee("Juana", 22000)
        eustaquia = ProductOwner("Eustaquia", 30000, "Hawaiana", 10)

        employees = [pepe, juana]
        product_owner = eustaquia

        return Shop(employees, product_owner)

    def add_pizza(self, pizza, price):
        self.pizzas[pizza] = price
