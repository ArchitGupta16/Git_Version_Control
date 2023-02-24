from Subtraction import subtract
from Multiplication import multi
from Division import division
from Add import add

print("MENU\n1.Add\n2.Subtract\n3.Multiplication\n4.Divide\n5.Exit")
choice = int(input("Enter your choice:"))

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))


cont = "y"
while choice in range(1,6) and cont.lower=="y":
    if choice == 1:
        print("Addition:",add(a,b))
    elif choice == 2:
        print("Subtraction:",subtract(a,b))
    elif choice == 3:
        print("Multiplication", multi(a,b))
    elif choice == 4:
        print("Division",division(a,b))
    else:
        print("Invalid Choice!!")
        exit()
    cont=input("Do you want to continue?(Y/N):")
