from Subtraction import subtract
from Multiplication import multi
from Division import division
from Add import add
from Power import power
from SquareRoot import squareRoot
from Logarithm import logarithm

print("MENU\n1.Add\n2.Subtract\n3.Multiplication\n4.Divide\n5.Square root\n6.Logarithm\n7.Power\n8.Exit")
choice = int(input("Enter your choice:"))

cont = "y"
while choice in range(1,8) and cont.lower()=="y":
    if choice == 1:
        print("Addition:",add())
    elif choice == 2:
        print("Subtraction:",subtract())
    elif choice == 3:
        print("Multiplication", multi())
    elif choice == 4:
        print("Division",division())
    elif choice == 5:
        print("Square root", squareRoot())
    elif choice == 6:
        print("Logarithm", logarithm())
    elif choice == 7:
        print("Power", power())

    else:
        print("Invalid Choice!!")
        exit()
    cont=input("Do you want to continue?(Y/N):")
    choice = int(input("Enter your choice:"))

