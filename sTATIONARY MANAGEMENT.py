
import tkinter as tk

from tkinter import ttk, messagebox

class StationeryOrderManagment:

    def __init__(self, root):

        self.root = root

        root.title("Stationery Order Management App")

        root.configure(bg="#d0efff")


        self.items = {"NOTEBOOK": 3, "PENCIL PACK": 2, "PEN SET": 4,
                      
                      "ERASER": 1, "GEOMETRY BOX": 6, "COLOUR PENCILS": 5}
        
        self.rate = 82


        frame = ttk.Frame(root)

        frame.place(relx=0.5, rely=0.5, anchor="center")


        ttk.Label(frame, text="Stationery Order Management",
                  
                  font=("Arial", 20, "bold")).pack(pady=10)
        

        self.labels = {}

        for item, price in self.items.items():

            self.labels[item] = ttk.Label(frame, text=f"{item}: ${price}")

            self.labels[item].pack(pady=5)


        self.currency = tk.StringVar(value="USD")

        ttk.Label(frame, text="Currency:").pack()

        dropdown = ttk.Combobox(frame, textvariable=self.currency,
                                
                                values=["USD", "INR"], state="readonly")
        
        dropdown.pack()
        self.currency.trace("w", self.update_prices)

        ttk.Button(frame, text="Place Order", command=self.place_order).pack(pady=10)

    def update_prices(self, *args):

        symbol = "₹" if self.currency.get() == "INR" else "$"

        rate = self.rate if self.currency.get() == "INR" else 1


        for item in self.items:

            self.labels[item].config(text=f"{item}: {symbol}{self.items[item]*rate}")


    def place_order(self):

        symbol = "₹" if self.currency.get() == "INR" else "$"

        rate = self.rate if self.currency.get() == "INR" else 1

        total = sum(self.items.values()) * rate


        messagebox.showinfo("Order Placed", f"All stationery items ordered!\nTotal Cost: {symbol}{total}")

root = tk.Tk()

root.geometry("800x600")

app = StationeryOrderManagment(root)

root.mainloop()
