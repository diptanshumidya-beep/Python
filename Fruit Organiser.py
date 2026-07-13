basket1 = {"apple","banana", "mango","apple","grape"}

basket2 = { "mango","kiwi","mango","kiwi"}

print("Basket 1:" ,basket1)
print("Basket 2:" ,basket2)

basket1.add("orange")
print("basket 1 after ading orange",basket1)


common_fruits =  basket1.intersection(basket2)
print ("Fruits count array:",common_fruits)

import array as arr

fruit_counts = arr.array('i',[3,5,4,1])
print("Fruits count array",fruit_counts)

fruit_counts.insert(0,1)
fruit_counts.append(6)

print("Fruit count after adding items:",fruit_counts)

count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears:",count_of_4)


fruit_counts.reverse()
print("Reversed fruits count away:",fruit_counts)


print("")

print("================ CLASS FRUIT BASKET ORGANIZER===================")

print("bASKET 1:",basket1)

print("bASKET 2:",basket2)

print("Shared fruits:",common_fruits)

print("Fruit counts:",fruit_counts)

print ("=========================================")

