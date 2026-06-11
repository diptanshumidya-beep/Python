def add (P,Q):
    return P + Q

def subtract (P,Q):
    return P - Q

def multiply (P,Q):
    return P * Q

def divide (P,Q):
    return P / Q


print ("Please select the operation")

print ("a.add")

print ("b.subtarct")

print ("c.multiply")

print ("d.divide")

choice = input ("Please enter the choice(a,b,c,d):")

num_1 = int (input("ENTER THE FIRST NUMBER"))

num_2 = int (input("ENTER THE SECOND NUMBER"))


if choice == 'a':
    print (add(num_1,num_2))

elif choice == 'b':
    print (subtract(num_1,num_2))

elif choice == 'c':
    print (multiply(num_1,num_2))


elif choice == 'd':
    print (divide(num_1,num_2))


else:
    print("This is invalid input")









