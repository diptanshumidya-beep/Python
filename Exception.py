try:
    num1, num2 = eval(input("Enter two numbers , seperated by a comma :"))

    result = num1 / num2
    print ("Result is", result)

except ZeroDivisionError:
    print("You donkey dont give 0 as divisor.Pi om baba will keep you in jail!!!!!!!!!!!!!!!!!!!")


except SyntaxError:
    print("Comma is missing.Enter numbers nicelty.")

except:
    print("Wrong input")


else:
    print("NO exceptions")

finally:
    print("This will execute no matter what")



