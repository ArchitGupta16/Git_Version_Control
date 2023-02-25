def division():
    a = int(input("Enter number 1:"))
    b = int(input("Enter number 2:"))
    while b==0:
        print("Cannot divide by zero!\nPlease enter again")
        b = int(input("Enter number 2 again:"))
    return a / b
