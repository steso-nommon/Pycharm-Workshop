#!/usr/bin/python3

"""
 Module description: a
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

from nommon_pizza.items.pizza_design import PizzaDesign


class Pizza:
    PIZZA_STATUS_HOT = "hot"
    PIZZA_STATUS_COLD = "cold"

    def __init__(self, pizza_design: PizzaDesign, status: str):
        self.pizza_design = pizza_design
        if status != Pizza.PIZZA_STATUS_COLD and status != Pizza.PIZZA_STATUS_HOT:
            raise ValueError("Pizza cannot be in that status.")
        self.status = status

    def __str__(self):
        return f"Pizza: {self.pizza_design.pizza_name} | status={self.status}"
