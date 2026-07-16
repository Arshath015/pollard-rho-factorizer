import pytest
from core.pollard_rho import PollardRho

def test_factor_small_numbers():
    assert PollardRho.factor(10) == [2, 5]
    assert PollardRho.factor(15) == [3, 5]

def test_factor_large_numbers():
    assert PollardRho.factor(8051) == [97, 83]

def test_factor_prime_numbers():
    assert PollardRho.factor(23) is None