
from tkinter import *

from tkinter import messagebox

root = Tk()

root.title("Reading Schedule Planner")

root.configure(bg="light blue")

root.geometry("500x300")


Label(root, text="Reading Schedule Planner", font=("Arial", 18, "bold"), bg="light blue").pack(pady=50)

Label(root, text="Create a simple plan to complete your book.", bg="light blue").pack()


def topwin():

    top = Toplevel(root)

    top.title("Create Reading Plan")

    top.geometry("500x350+50+50")

    top.configure(bg="light grey")


    Label(top, text="Enter total number of pages:").place(x=80, y=40)

    pages = Entry(top)

    pages.place(x=280, y=40)


    Label(top, text="Pages you can read each day:").place(x=80, y=90)

    daily = Entry(top)

    daily.place(x=280, y=90)


    Label(top, text="Your Reading Plan", font=("Arial", 14, "bold")).place(x=175, y=185)

    Label(top, text="Complete reading days:").place(x=80, y=235)

    days = Entry(top)

    days.place(x=280, y=235)


    Label(top, text="Pages remaining:").place(x=80, y=275)

    remaining = Entry(top)

    remaining.place(x=280, y=275)


    def calculate():

        try:
            total = int(pages.get())

            per_day = int(daily.get())


            if total <= 0 or per_day <= 0:

                messagebox.showerror("Error", "Enter numbers greater than zero.")

                return

            days.delete(0, END)

            remaining.delete(0, END)

            days.insert(END, total // per_day)

            remaining.insert(END, total % per_day)


        except ValueError:

            messagebox.showerror("Error", "Enter valid whole numbers.")


    Button(top, text="Create Plan", command=calculate, bg="#1261A0", fg="white").place(x=205, y=135)


Button(root, text="Create My Reading Plan", command=topwin, bg="#1261A0", fg="white").pack(pady=15)


root.mainloop()
