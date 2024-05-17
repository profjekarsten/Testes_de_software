import pytest

from myapp.app import multiply_by_two, divide_by_two


class TestApp:
    def test_multiplication(self):
        res = multiply_by_two(10)
        assert res == 20

    def test_division(self):
        res = divide_by_two(10)
        assert res == 10
