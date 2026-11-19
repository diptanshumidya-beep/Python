
from tkinter import *

from tkinter import messagebox




window = Tk()

window.title("After-School Routine Checker")

window.geometry("400x320")



Label(window, text="My After-School Routine", font=("Arial", 16, "bold")).pack(pady=10)

Label(window, text="Enter your next after-school task:").pack()



task_entr = Entry(window, width=35)

task_entr.pack(pady=8)



key_label = Label(window, text="Last key pressed: None")

key_label.pack(pady=5)


def handle_key(event):

    key_label.config(text="Last key pressed: " + event.char)


task_entr.bind("<Key>", handle_key)



routine_msg = Label(window, text="Click here to check your routine", bg="#d0efff", width=32, height=3)

routine_msg.pack(pady=10)



def handle_click(event):


    routine_msg.config(text="Routine area selected!")


routine_msg.bind("<Button-1>", handle_click)


def check_routine():

    task = task_entr.get()


    if task == "":

        messagebox.showwarning("Missing Task", "Please enter an after-school task.")

    else:

        routine_msg.config(text="Next task: " + task)


Button(window, text="Check My Routine", command=check_routine).pack(pady=10)




window.mainloop()
