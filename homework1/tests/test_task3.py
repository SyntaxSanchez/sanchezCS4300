# test_task3.py

import pytest
from task3 import numberSignCheck, primesTen, sum_1_to_100, isPrime

def test_check_number_sign():
    assert numberSignCheck(10) == "positive"
    assert numberSignCheck(-5) == "negative"
    assert numberSignCheck(0) == "zero"

def test_get_first_10_primes():
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primesTen() == expected_primes

def test_sum_1_to_100():
    assert sum_1_to_100() == 5050  # Known formula result: n(n+1)/2

def test_is_prime():
    assert isPrime(2) is True
    assert isPrime(17) is True
    assert isPrime(18) is False
    assert isPrime(1) is False
    assert isPrime(0) is False
    assert isPrime(-3) is False

