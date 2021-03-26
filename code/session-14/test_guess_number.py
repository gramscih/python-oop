import guess_number as guess

from unittest import mock

@mock.patch("guess_number.dice.roll_dice")
def test_guess_num(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess.guess_num(3) == "You won!"