Grade = {"Mia Bhai" : 73 , "Dhoni" : 7 , "Pi Om Baba" : 31 , "Boom Boom" : 93 , "Roko" : 63}

print(Grade)


print(len(Grade))

length = (len(Grade))

a = 0

for i in Grade:
     
     i = Grade[i]

     a = a+ i

print(a)

average = a / length

print("average =" , average )






d = 0

for i in Grade:
    if Grade[i] > d:
        d = Grade[i]

print("The highest score is", d)
     






print("Score tracker")

print("1 = Mia Bhai  , 2 = Dhoni  ,  3 = PiomBaba  , 4 = Boom Boom  , 5  = Roko")

namee = input("Give a option from above ").strip()


if namee == "1":
     print(Grade["Mia Bhai"])

if namee == "2":
     print(Grade["Dhoni"])

if namee == "3":
     print(Grade["Pi Om Baba"])

if namee == "4":
     print(Grade["Boom Boom"])

if namee == "5":
     print(Grade["Roko"])





