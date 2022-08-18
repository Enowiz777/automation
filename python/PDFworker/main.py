# External imports
from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
import os

# Imports from local
from tkinter.filedialog import askopenfile
from page_input_to_numbers import convert_to_num_list
from pdfmerge import merge_pdfs

main_window = Tk()
# Set the Title
main_window.title("PDFworker by Enoch Park")
# Set Windows Size
main_window.geometry("500x500")

# Glboal variables
ROW = 0
user_input_list = []
output_path =""

# Getter

def open_file():
    global ROW
    global main_window
    global user_input_list
    
    dict = {}
    if ROW < 10:
    # Get the file location from the user
        file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.pdf')])

    # Extract the absolute path of the file.
    if file:
        # Get absolute filepath; Add to dict
        filepath = os.path.abspath(file.name)   
        dict["path"]= filepath

        # Get the file name
        divide = file.name.split("/")
        last_index = len(divide) -1
        filename = divide[last_index]
        
        ROW+=1
        Label(main_window, text="File Selected: " + str(filename)).grid(row=ROW, columnspan=3, padx=0)

        ROW+=1
        Label(main_window, text="Page Range:").grid(row=ROW, column=0, padx=0)
        user_input = Entry(main_window)
        
        # Get input; Add to dict
        dict["input"]= user_input
        user_input_list.append(dict)
        user_input.grid(row=ROW, column=1, padx=0)

    else:
        Label(main_window, text="You can't add more files than 5 pdf files.").grid(row=0, column=1)

def merge_file():
    # Iterate list of dictionaries and update the input value.
    for item in user_input_list:
        item["input"] = item["input"].get()

    # Convert input to list of pages
    for item in user_input_list:
        pages = convert_to_num_list(item["input"])
        item["pages"]= pages

    print(user_input_list)
    merge_pdfs(user_input_list, output_path)


def output_file():
    global output_path
    output_directory = filedialog.askdirectory()
    label = Label(main_window, text=f"Path selected: {output_directory}")
    label.place(x=20, y=430)
    output_path=output_directory

# Buttons
browser_button = Button(main_window, text="Browse", command=open_file)
browser_button.grid(row=ROW,column=0)

output_button = Button(main_window, text="Select Output Folder", command=output_file)
output_button.place(x=20, y=400)

merge_button = Button(main_window, text="Merge", command=merge_file)
merge_button.place(x=230, y=450)


# Text Input
main_window.mainloop()