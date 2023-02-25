import math


def logarithm():
    a = int(input("Enter number to calculate log : "))
    if a > 0:
        return math.log(a)
    else:
        return "Invalid Input !!"
