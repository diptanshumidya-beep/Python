def cube(number):
   return number**3

def divison(number):
   if number%3==0:
      return (cube(number))
   else:
      return("die")

print(divison(9))
print(divison(4))