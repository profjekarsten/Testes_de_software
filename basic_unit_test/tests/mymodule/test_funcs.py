import pytest

from myapp.mymodule.funcs import *

def test_add():
    # This test will fail.
    assert add(4, 8) == 14

def test_subtract():
    assert subtract(3, 6) == -3

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(56, 8) == 7
