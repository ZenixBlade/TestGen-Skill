def add(a, b):
    return a + b

def add(a, b):
    return a + b

import pytest

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_mixed_numbers():
    assert add(1, -2) == -1

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 1) == 1
    assert add(0, -1) == -1

def test_add_large_numbers():
    assert add(10, 20) == 30
    assert add(-10, 20) == 10

def test_add_zero_and_positive_number():
    assert add(0, 1) == 1

def test_add_zero_and_negative_number():
    assert add(0, -1) == -1

def test_add_invalid_input():
    with pytest.raises(TypeError):
        add("a", 1)

def test_add_mismatched_types():
    with pytest.raises(TypeError):
        add(1, "a")

def test_add_negative_with_zero():
    assert add(-1, 0) == -1
