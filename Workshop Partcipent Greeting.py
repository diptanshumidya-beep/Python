
from tkinter import *

from datetime import date




root = Tk()

root.title("Workshop Participant Greeting")

root.geometry("400x300")



Label(root, text="Workshop Welcome Desk", fg="white", bg="#072F5F").pack()


Label(root, text="Participant Name", bg="#3895D3").pack(pady=10)

name_entr = Entry(root)

name_entr.pack()



text_box = Text(root, height=4, width=40)



def welcom():

    text_box.delete("1.0", END)

    text_box.insert(END, "Hello {name_entr.get()}Welcome to the workshop.\nDate: {date.today()}")




Button(root, text="Check In", command=welcom, bg="#1261A0", fg="white").pack(pady=10)

text_box.pack()


root.mainloop()
