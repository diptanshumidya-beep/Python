
try:

    def add (a,b):
       return a+b

    def subtract (a,b):
        return a-b

    def multiply (a,b):
        return a*b

    def divide (a,b):
        return a/b

    print("This is a calculator")

    print("For addition choose a")

    print("For subtraction choose b")

    print("For multiplication choose c")

    print("For division choose d")

    choice = print(input("Enter your choice"))

    a = print(int(input("Enter number one ")))

    b = print(int(input("Enter number two ")))


    if choice  == "a":
        print("Your sum is", add(a,b))


    elif choice == "b":
        print("Your subtracted answer is",subtract(a,b))

    elif choice == "c":
        print("Your product is",multiply(a,b))

    elif choice == "d":
        print("Your qoutient is",divide(a,b))

except:
    ZeroDivisionError
    print("You cant divide by 0")

    ValueError
    print("Only give the choice in small letters only.And only give the input of given choices")




