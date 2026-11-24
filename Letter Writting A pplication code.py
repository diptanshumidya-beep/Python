from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.title("Letter Writing Application")
root.geometry("600x500")

root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

def open_letter():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return

    txt_edit.delete("1.0", END)
    with open(filepath, "r") as file:
        txt_edit.insert(END, file.read())

    root.title(filepath)

def save_letter():
    filepath = asksaveasfilename(defaultextension=".txt")
    if not filepath:
        return

    with open(filepath, "w") as file:
        file.write(txt_edit.get("1.0", END))

    root.title(filepath)

txt_edit = Text(root)
fr_buttons = Frame(root, relief=RAISED, bd=2)

btn_open = Button(fr_buttons, text="Open Letter", command=open_letter)
btn_save = Button(fr_buttons, text="Save Letter As...", command=save_letter)

btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

root.mainloop()