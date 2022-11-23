#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'


class Pizza:
    PIZZA_STATUS_HOT = "hot"
    PIZZA_STATUS_COLD = "cold"

    def __init__(self, pizza_type: str, status: str):
        self.pizza_type = pizza_type
        if status != Pizza.PIZZA_STATUS_COLD or status != Pizza.PIZZA_STATUS_HOT:
            raise ValueError("Pizza cannot be in that status.")
        self.status = status

    def __str__(self):
        return f"Pizza: {self.pizza_type} | status={self.status}"
