

import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri","Sat"]

scores = [20,85,60,50,77,777]


plt.plot(days,scores)

plt.show()



plt.plot(days,scores)

plt.title("My Quiz Score Tracker")

plt.xlabel("Day of the week")

plt.ylabel("SCORE")

plt.ylim(0,100)

plt.show()



plt.plot(days,scores , color="blue" , marker = "D" , linestyle = "dashed",linewidth = 7 )

plt.title("My Quiz Score Tracker")

plt.xlabel("Day of the week")

plt.ylabel("SCORE")

plt.ylim(0,100)

plt.show()


plt.bar(days,scores , color="red" )

plt.title("My Quiz Score Tracker")

plt.xlabel("Day of the week")

plt.ylabel("SCORE")

plt.ylim(0,100)

plt.show()






















