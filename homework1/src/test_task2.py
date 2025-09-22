
import pytest
from task2 import integer, floating, string

# Test integer
def test_integer_type():
    assert isinstance(integer(), int)
def test_integer_value():
    assert integer() == 2

# Test float
def test_floating_type():
    assert isinstance(floating(), float)
def test_floating_value():
    assert floating() == 4.6

# Test string
def test_string_type():
    assert isinstance(string(), str)
def test_string_value():
    assert string() == "Hello, there"

