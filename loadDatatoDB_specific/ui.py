import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
import threading
from loadDatatoDB import loadDatatoDB
import sys

DB_NAME = "presupuesto"
TABLE_NAME = "data"

class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.insert(tk.END, str)
        self.widget.see(tk.END)

    def flush(self):
        pass

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def start_process():
    input_file = file_entry.get()
    input_yr = input_yr_entry.get()

    sys.stdout = TextRedirector(output_text)

    threading.Thread(target=loadDatatoDB, args=(input_file, DB_NAME, TABLE_NAME, input_yr), daemon=True).start()

root = tk.Tk()
root.title("Discover 0.0.1")

tk.Label(root, text="Excel File:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Year:").grid(row=1, column=0, padx=10, pady=10)
input_yr_entry = tk.Entry(root, width=50)
input_yr_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Start Process", command=start_process).grid(row=2, column=1, padx=10, pady=10)

output_text = scrolledtext.ScrolledText(root, height=10)
output_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()