# test_task4.py
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from task4 import calculate_discount

# Test function to calculate the applied price and applied discount 
# handling both integer and floating-point values
def test_calculate_discount():
    assert calculate_discount(100,50) == 50
    assert calculate_discount (20.50, 10.0) == 18.45
    assert calculate_discount (10, 10.5) == 8.95
    assert calculate_discount (25.5, 20) == 20.4


