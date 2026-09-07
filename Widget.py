from tkinter import *

from datetime import date



root = Tk()

root. title ("Getting started with widgets")

root.geometry ('400x300')



lbl = Label(text = "Hey There!", fg = "#A1CAB2", bg ="#A80909", height= 1, width = 300 )

name_lbl = Label(text = "Fulll Name" , bg = "#02272E")

name_entry = Entry()



def display():

    name = name_entry.get()



    global message 


    message = "Welcome to the Application \n Today's date is"


    greet = "Hello  "+ name + "\n"



    text_box.insert (END,greet)

    text_box.insert (END, message)

    text_box.insert (END, date.today())



text_box = Text(height= 3)


btn = Button(text = "Begin", command = display , height = 1, bg = "#F8E003" , fg = "#020202")



lbl.pack()

name_lbl.pack()


name_entry.pack()

btn.pack ()

text_box.pack()






root.mainloop ()






