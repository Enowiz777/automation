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

def open_ui(): 
  Merge_button = False
  user_input_list = []
  def open_file():
      global ROW
      global main_window
      global user_input
      if ROW < 10:
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
          user_input = Entry(main_window)
          user_input_list.append(user_input)
          user_input.grid(row=ROW, column=1, padx=0)
      else:
        Label(main_window, text="You can't add more files than 5 pdf files.").grid(row=0, column=1)

  def merge_file():
    global Merge_button
    Merge_button=True

  def output_file():
    print("")

  if Merge_button:
    return user_input_list
  # Button
  browser_button = Button(main_window, text="Browse", command=open_file)
  browser_button.grid(row=ROW,column=0)

  output_button = Button(main_window, text="Browse", command=output_file)
  output_button.place(x=20, y=400)

  merge_button = Button(main_window, text="Merge", command=merge_file)
  merge_button.place(x=230, y=450)

  # Label

  # Text Input
  main_window.mainloop()