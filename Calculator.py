print("MENU\n1.Add\n2.Subtract\n3.Multiplication\n4.Divide\n5.Exit")
choice = int(input("Enter your choice:"))

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

def add(a,b):
    return a+b
def sub(a,b):
    return (a-b)

def mul(a,b):
    return (a*b)

def div(a, b):
    return a/b

cont = "Y"
while choice in range(1,6) and cont=="Y":
    if choice == 1:
        print("Addition:",add(a,b))
    elif choice == 2:
        print("Subtraction:",sub(a,b))
    elif choice == 3:
        print("Multiplication",mul(a,b))
    elif choice == 4:
        print("Division",div(a,b))
    else:
        print("Invalid Choice!!")
        exit()
    cont=input("Do you want to continue?(Y/N):")
