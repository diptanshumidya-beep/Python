import pandas as pd

print ("Part 1: Panda Series")

scores = [98500 , 82800 , 26400 , 65100 , 54800]

players = pd.Series(scores , index = [ "Nightwolf", "Starfire" , "Pixel King" , "Cyber Fox" , "Transform"])

print(players)


print()

print (" PART 2 : PANDAS DATAFRAME")

data = {

    "Player": ["Night Wolf", "Starfire", "Pixel King", "Cyber Fox", "Transform"],

    "Level" : [42 , 38 , 35 , 30 , 27],

    "Score" : [98500 , 82800 , 26400 , 65100 , 54800],

    "Wins"  : [210,185,162,140,118]
}


df = pd.DataFrame(data)
print (df)



print()

print ( "PART 3 : ACESSING ROWS")

print("Row0 (top player) :")

print(df.loc[0])

print()

print("Rows2 and 3:")

print(df.loc[2:3])



print()

print ("PART 4: Readin a CSV File")

full_df = pd.read_csv("leaderboard.csv")


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









