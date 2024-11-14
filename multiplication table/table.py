import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#functions

def generate_tables():
    selected_option = int(dropdown.get())  
    range_value = int(stringvariable.get())
   
    output_text.delete("1.0", tk.END)
     
    output_text.insert(tk.END, f"Multiplication Table for {selected_option} up to {range_value}\n\n")
    for i in range(1, range_value + 1):
        result = selected_option * i
        output_text.insert(tk.END, f"{selected_option} x {i} = {result}\n")

#window

window=tk.Tk()
window.title("Mathematical table generator")
window.geometry("500x600")

#title label and nr+range label

title=tk.Label(window, text=("Multiplication Table"), font=("Arial", 10))
title.place(x=175, y=0)    

text=tk.Label(window, text=("Number and Range:"), font=("Arial", 10))
text.place(x=10, y=50)

#dropdown/ combobox

dropdown=ttk.Combobox(window, width=20, values=["5","10","15","20","25","30","35","40","45","50"])
dropdown.place(x=175,y=50)

#radio buttons

stringvariable=tk.StringVar(value="value")

ten=tk.Radiobutton(window, text="10",variable=stringvariable, value="10")
ten.place(x=400, y=50)

twenty=tk.Radiobutton(window, text="20",variable=stringvariable, value="20")
twenty.place(x=400, y=75)

thirty=tk.Radiobutton(window, text="30",variable=stringvariable, value="30")
thirty.place(x=400, y=100)

fourty=tk.Radiobutton(window, text="40",variable=stringvariable, value="40")
fourty.place(x=400, y=125)

fifty=tk.Radiobutton(window, text="50",variable=stringvariable, value="50")
fifty.place(x=400, y=150)

#button

generate=tk.Button(window, text="Generate", command=generate_tables)
generate.place(x=200,y=90)

#output tables

output_text = tk.Text(window, width=40, height=20)
output_text.place(x=80, y=150)

window.mainloop()