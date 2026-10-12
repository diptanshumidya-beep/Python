import matplotlib.pyplot as plt

weeks = ["Week1","Week2","Week3","Week4","Week5"]

money = [2500,3000,7000,15500,1000,]


plt.plot(weeks,money)

plt.show()



plt.plot(weeks,money)

plt.title("My Weekly Savings Tracker")

plt.xlabel("No of the Week")

plt.ylabel("My Savings")

plt.ylim(0,16000)

plt.show()



plt.plot(weeks,money , color="green" , marker = "*" , linestyle = "dashed",linewidth = 1 )

plt.title("My Weekly Savings Tracker")

plt.xlabel("No of the Week")

plt.ylabel("My Savings")

plt.ylim(0,16000)

plt.show()


plt.bar(weeks,money , color="red" )

plt.title("My Weekly Savings Tracker")

plt.xlabel("No of the Week")

plt.ylabel("My Savings")

plt.ylim(0,16000)

plt.show()

