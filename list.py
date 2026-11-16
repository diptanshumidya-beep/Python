
marks = [123 , 98 , 67 , 69 , 200 , 78 , 55 ]

print(marks)

print(len(marks))

print(marks [2])


print(marks [0 :2:2])

for i in range (len(marks)):
    print("Marks")
    print("The students apperaed for exam are" , len(marks))

j = 0

for ii in marks:
    j = ii + j

marks . sort()

print("highest mark" , marks[-1])

print("smallest mark" , marks[0])

print("average is " , j / len(marks))

print("sum is" , j)