import sys

sys.path.append('./src')
sys.path.append('../')

import pytest
import proj_calc.src.calc as tf


# Unit test for calc_sum function
def get_data_test_calc_sum():
    return [("1/2", 2.0, 2.5), (0.5, "10/20", 1), (2, 2, 4),
            ("3", "2", 5)]


@pytest.mark.parametrize('a, b, expected', get_data_test_calc_sum())
def test_calc_sum_parametrize(a, b, expected):
    assert tf.calc_sum(a, b) == expected


# Unit test for calc_multiplication function
def get_data_test_calc_multiplication():
    return [("2", "1/2", 1), ("1/2", "10/20", 0.25), ("5", "2", 10),
            ("3", "2", 6)]


@pytest.mark.parametrize('a, b, expected', get_data_test_calc_multiplication())
def test_calc_multiplication_parametrize(a, b, expected):
    assert tf.calc_multiplication(a, b) == expected