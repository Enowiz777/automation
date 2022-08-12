# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("1050x700")

# Path list
path_list = []

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
   if file:
      filepath = os.path.abspath(file.name)
      path_list.append(filepath)
      Label(win, text="The PDF File is located at : " + str(filepath), font=('Aerial 11')).pack(side="top", pady=10)
      Label(win, text="Page Range:").pack(side="top")
      Entry(win).pack(side="top")


# Add a Label widget
label = Label(win, text="Please Add path of PDF files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()