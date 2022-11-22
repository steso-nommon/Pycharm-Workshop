#!/usr/bin/python3

"""
 Module description: 
"""

__author__ = 'steso'
__copyright__ = '(c) Nommon 2022'

import pytest

from nommon_pizza.shop.shop import Shop


def setup_function():
    """
    DESCRIPTION:
        Setup any state tied to the execution of the given function.
            Invoked for every test function in the module.
    """
    pass


def teardown_function():
    """
    DESCRIPTION:
        Teardown any state that was previously setup with a setup_function call.
    """
    pass


@pytest.fixture
def nommon_shop():
    shop = Shop.create_shop()
    yield shop


@pytest.mark.parametrize('salary_adjust', [1.2, 1.5, 0, 1.8])
def test_adjust_salaries(salary_adjust, nommon_shop):
    """
    DESCRIPTION:
        Test description.
    INPUT:
        foo_configuration.cfg configuration file for foo module.
        example_data.csv input data needed.
    EXPECTED OUTPUT:
        results file with the example data processed.
    STEPS:
        1. First step
        2. Final step
    """

    return_code = nommon_shop.adjust_salaries(salary_adjust)

    assert return_code == "OK"


