L = [1,2,3,4,5,6,7,7,8,9,0,133,45,6,8,3835,5,6,7,7,82,4,534,6,6]

print("oRIGINAL LIST IS:",L)

count = 0

for i in L:
    count += i


avg = count/len(L)

print("Suum is =",count)

print ("Average =",avg)

L.sort()

print("SMALLLEST ELEMENT IS:",L[0])

print ("LARGEST ELEMENT IS",L[-1])




