
from tkinter import *



root = Tk()

root.title("ATM PIN Setup Interface")

root.geometry("400x500")




details = Frame(root, bg="#d0efff")

details.place(x=20, y=10, width=360, height=150)




Label(details, text="Account Name", bg="#3895D3", fg="white").place(x=15, y=25)

name_entry = Entry(details)

name_entry.place(x=155, y=25)



Label(details, text="Create PIN", bg="#3895D3", fg="white").place(x=15, y=85)

pin_entry = Entry(details, show="*")

pin_entry.place(x=155, y=85)




message = Text(root, height=5, width=42, bg="#BEBEBE")

message.place(x=25, y=410)




def confirm_pin():

    message.delete("1.0", END)



    if name_entry.get() == "" or pin_entry.get() == "":

        message.insert(END, "Please enter account name and PIN.")



    else:

        message.insert(END, f"Hello {name_entry.get()}!\nYour ATM PIN has been set successfully.")





numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["Clear", 0, "Enter"]]



keypad = Frame(root, relief=SUNKEN, borderwidth=2)

keypad.place(x=85, y=180)




for i in range(4):



    for j in range(3):

        Label(keypad, text=numbers[i][j], bg="#d0efff", width=8, height=2, relief=RAISED).grid(row=i, column=j)




Button(root, text="Set ATM PIN", command=confirm_pin, bg="red", fg="white").place(x=145, y=370)


root.mainloop()
