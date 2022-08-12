# Necessary imports
from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from tkinter.filedialog import askopenfile
import os

main_window = Tk()
ROW = 0

def open_file():
    global ROW
    ROW+=1
    # Get the file location from the user
    file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])

    # Extract the absolute path of the file.
    if file:
      filepath = os.path.abspath(file.name)   
      
      # Get the file name
      divide = file.name.split("/")
      last_index = len(divide) -1
      filename = divide[last_index]

      Label(main_window, text="File Selected: " + str(filename)).grid(row=ROW, column=1, padx=0)
      
      ROW+=1
      Label(main_window, text="Page Range:").grid(row=ROW, column=0, padx=0)
      Entry(main_window).grid(row=ROW, column=1)
# Button
Button(main_window, text="Browse", command=open_file).grid(row=ROW, column=0)

# Label
# Label(main_window, text= "Hello World").grid(row=1, column=1)
# Label(main_window, text="tjdsklafj").grid(row=1, column=2)


# Text Input


main_window.mainloop()
