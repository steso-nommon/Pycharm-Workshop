#!/usr/bin/python3

"""
 Module description: papapa
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.people.employee import Employee
from nommon_pizza.people.product_owner import ProductOwner


class Shop:

    def __init__(self, employees, product_owner):
        self.employees = employees
        self.product_owner = product_owner
        self.pizzas = dict()
        self.inventory = dict()

    @staticmethod
    def create_shop():
        pepe = Employee("Pepe", 20000)
        juana = Employee("Juana", 22000)
        eustaquia = ProductOwner("Eustaquia", 30000, "Hawaiana", 10)

        employees = {"Juana": juana,
                     "Pepe": pepe}
        product_owner = eustaquia

        return Shop(employees, product_owner)

    def create_pizza_design(self, pizza, price):
        self.pizzas[pizza] = price

    def adjust_salaries(self, salary_adjust_percentage):
        for employee in self.employees.values():
            employee.salary *= salary_adjust_percentage

        try:
            self.product_owner.salary /= salary_adjust_percentage
        except ZeroDivisionError:
            raise ValueError("Zero division done.")

        return "OK"
