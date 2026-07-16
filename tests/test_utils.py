import pytest
from core.utils import Utils

def test_is_prime_small_numbers():
    assert Utils.is_prime(10) is False
    assert Utils.is_prime(11) is True

def test_is_prime_large_numbers():
    assert Utils.is_prime(23) is True
    assert Utils.is_prime(24) is False