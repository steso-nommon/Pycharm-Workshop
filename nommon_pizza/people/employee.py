#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.people.person import Person
from nommon_pizza.items.pizza import Pizza


class Employee(Person):

    def __init__(self, name: str, salary: int):
        super().__init__(name)
        self.salary = salary

    def create_pizza(self, pizza, status):
        return Pizza(pizza, status)
