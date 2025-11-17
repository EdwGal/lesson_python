# Import the required libraries
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x470")

# load the image and convert it into Tkinter Photoimage
bg=ImageTk.PhotoImage(file="login.png")

# Add a label widget to display the image
label=Label(win, image=bg)
label.place(x=0, y=0)

win.mainloop()