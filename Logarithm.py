import math

def logarithm():
    a = int(input("Enter number to calculate log : "))
    if a > 0:
        print(math.log(a))
    else:
        print("Invalid Input !!")