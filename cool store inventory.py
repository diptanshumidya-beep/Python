items = ["pencil","eraser","notebook","sharpner","glue",]

stock_counts = [12,0,8,5,3]

inventory = {item:count for item, count in zip(items,stock_counts)}

print ("Full inventory",inventory)


in_stock_items =  [item for item in items if inventory[item] > 0]
print("Items in stock",in_stock_items)


choosen_item = input("Which item do you want to buy?")

if choosen_item not in inventory or inventory [choosen_item] == 0:
    print(choosen_item,"is out of stock! Stopping the checker")
    exit()

prices = [10,5,40,15,20]
markup = int(input("ENTER THE MARKUP AMMOUNT TO ADD TO EVERY PRICE:"))

marked_up_prices = list(map(lambda p: p + markup, prices))
print ("Marked UP PRICES:", marked_up_prices)


item_index = items.index(choosen_item)
choosen_price = marked_up_prices[item_index]
print ("Price of", choosen_item, "purchased! Remainig stock",inventory[choosen_item])



print("")

print ("================================================SCHHOL INVENTORY CHECKER===============================================================")

print ("Item Brought",choosen_item)

print ("Price paid",choosen_price)

print ("Updated inventory",inventory)

print("===========================================================================================================================================================================================================")





