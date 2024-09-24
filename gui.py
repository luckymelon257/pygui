import tkinter as tk
from tkinter import ttk
import json

# Load JSON data from file
with open("data.json", "r") as file:
    data = json.load(file)

# Create GUI application
root = tk.Tk()
root.title("JSON Table")

# Create treeview table
tree = ttk.Treeview(root, columns=("Name", "Age", "Occupation"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Occupation", text="Occupation")

# Insert data into table
for entry in data:
    tree.insert("", "end", values=(entry["Name"], entry["Age"], entry["Occupation"]))

tree.pack(expand=True, fill="both")

# Run the application
root.mainloop()
