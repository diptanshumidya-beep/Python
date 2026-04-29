units = int(input("Please eneter number of units you ate:"))

if(units<50):
    ammount = units*2.60
    subcharge = 25

elif(units<=100):
    ammount = 130 + ((units-50)*3.25)
    subcharge = 35

elif(units<=200):
    ammount = 130 + 292.50 +((units-100)*5.26)
    subcharge = 45


else:
    ammount = 130 + 292.50 + 526 + ((units-200)*8.45)
    subcharge = 75


total = ammount+subcharge

print("You toatl bill = %.2f" %total)






