import pytest
import calculator as calc


# def test_add_integer():
#     assert calc.add(2, 3) == 5

# def test_add_string():
#     assert calc.add("2", "3") == "23"

# def test_add_list():
#     assert calc.add([1, 2], ["3"]) == [1, 2, '3']

params = [(2, 3, 5), ("2", "3", "23"), ([1,2], ["3"], [1, 2, "3"])]

@pytest.mark.parametrize("exp1, exp2, result", params)
def test_add(exp1, exp2, result):
    assert calc.add(exp1, exp2) == result

# class TestCalculator:
#     def test_add_integer(self):
#         assert calc.add(2, 3) == 5

#     def test_add_string(self):
#         assert calc.add("2", "3") == "23"

#     def test_add_list(self):
#         assert calc.add([1, 2], ["3"]) == [1, 2, '3']
