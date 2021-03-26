import calculator as calc
import pytest

def test_div():
    assert calc.divide(10, 2) == 5

def test_div_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(3, 0)