#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.people.person import Person


class Customer(Person):

    def __init__(self, name: str, wallet: int):
        super().__init__(name)
        self.wallet = wallet
