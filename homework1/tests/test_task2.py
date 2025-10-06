import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from task2 import integer, floating, string, boolean

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

def testBoolean():
    assert isinstance(boolean(),bool)

# parameterized test
@pytest.mark.parametrize("function, expected_type",
                         [
                         (integer, int),
                         (floating, float),
                         (string, str),
                         (boolean, bool),
                        ],
                    )
def testType(function, expected_type):
        assert isinstance(function(), expected_type)

