import pytest
from utils.calculator import add, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract_simple():
    assert subtract(1, 2) == -1
