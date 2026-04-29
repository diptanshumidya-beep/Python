MEDICAL = input("Did you have a medical cause for attending the exam? (Y/N):").strip().upper()

if MEDICAL == "Y":
    print("You are allowed to take the examination")

else:
    atten = int(input("Please enter your attendance in percentage"))

    if atten>= 75:
        print("You are allowed to take the examination")
    else:
        print("Not allowed")
























