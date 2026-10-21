import pandas as pd

print ("Part 1: MY FRIENDS MARKS")

Markas = [100, 47, 89 , 97 , 77]

players = pd.Series(Markas , index = [ "Dipuaana", "AnanthaLaxmiChaviti" , "RevanthBhai" , "Purajitho" , "Bob"])

print(players)


print()

print (" PART 2 : My Friends")

data = {

    "Friends": ["Dipuaana", "AnanthaLaxmiChaviti" , "RevanthBhai" , "Purajitho" , "Bob"],

    "Marks" : [100, 47, 89 , 97 , 77],

    "Passed Subjects" : [6 , 4 , 5 , 6 , 6],

    "Topped times"  : [777,0,29,432,10]
}


df = pd.DataFrame(data)
print (df)



print()

print ( "PART 3 : ACESSING FRIENDS")

print("Row0 (top player) :")

print(df.loc[0])

print()

print("Rows2 and 3:")

print(df.loc[2:3])


print()

print ("PART 4: Readin a CSV File")

full_df = pd.read_csv("studentmarks.csv")


print("First rows (head) :")
print(full_df.head())


print()

print("Last  1rows (tail):")
print(full_df.tail(3))


print()

print("Dataset info:")
print(full_df.info())

print()

print ("PART 5: CLEANING DATA")

print("Rows with missing valued removed(droped)")

clean_df = full_df.dropna()

print(clean_df.to_string())

print()

print("Missing Values filled with 0 (Fill na)")

filled_of = full_df.fillna(0)

print(filled_of.to_string)





