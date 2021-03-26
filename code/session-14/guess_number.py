import dice

def guess_num(num):
    result = dice.roll_dice()
    if num == result:
        print(f"Number: {result}")
        return "You won!"
    else:
        return "You lost!"