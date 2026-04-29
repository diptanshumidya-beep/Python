hieght = float(input("Enter your hieght in cm:"))

weight = float(input("Enter your hieght in kg:"))

BMIW = weight/ (hieght/100)**2


print ("Your BMI is",BMIW)


if BMIW <= 18.4:
    print("yOU ARE UNDERWEIGHT")

elif BMIW <= 24.9:
    print("You are healthy ")

elif BMIW <= 29.9:
    print("You are over weight")

elif BMIW <= 34.9:
    print("You are severly over weight")


elif BMIW <= 39.9:
    print("You are obeese")

else:
    print("You are severly obeese")

























