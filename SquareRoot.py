def squareRoot():
    a = int(input("Enter number to get Square root : "))
    while a<0:
        print ("Invalid Input!!Try Again")
        a = int(input("Enter number to get Square root : "))

    return a**(1/2)
