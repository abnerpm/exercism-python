import math


def isEven(number):
    return number % 2 == 0


def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    steps = 0

    while number > 1:
        if isEven(number):
            number = math.floor(number / 2)
        else:
            number = number * 3 + 1

        steps += 1

    return steps
