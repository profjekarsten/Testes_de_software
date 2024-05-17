import pytest

from myapp.mymodule.funcs import add

def test_add():
    res = add(10, 10)
    assert res == 20
