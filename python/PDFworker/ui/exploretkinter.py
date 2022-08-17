# Necessary imports
from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from tkinter.filedialog import askopenfile
import os

main_window = Tk()

# Set the Title
main_window.title("PDFworker by Enoch Park")
# Set Windows Size
main_window.geometry("500x500")


ROW = 0

def open_file():
    global ROW
    global main_window
    if ROW < 6:
      # Get the file location from the user
      file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.pdf')])

      # Extract the absolute path of the file.
      if file:
        filepath = os.path.abspath(file.name)   
        
        # Get the file name
        divide = file.name.split("/")
        last_index = len(divide) -1
        filename = divide[last_index]
        
        ROW+=1
        Label(main_window, text="File Selected: " + str(filename)).grid(row=ROW, columnspan=3, padx=0)

        ROW+=1
        Label(main_window, text="Page Range:").grid(row=ROW, column=0, padx=0)
        user_input = Entry(main_window).grid(row=ROW, column=1, padx=0)
        print(filepath)
        print(ROW)
    else:
      Label(main_window, text="You can't add more files than 5").grid(row=0, column=1)


def merge_file():
  print()


# Button
browser_button = Button(main_window, text="Browse", command=open_file)
browser_button.grid(row=ROW,column=0)

merge_button = Button(main_window, text="Merge", command=merge_file)
merge_button.place(x=230, y=450)

# Label
# Label(main_window, text= "Hello World").grid(row=1, column=1)
# Label(main_window, text="tjdsklafj").grid(row=1, column=2)


# Text Input


main_window.mainloop()
