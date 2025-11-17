from tkinter import *

raiz=Tk()
raiz.title("Calcular Pesos")
raiz.iconbitmap("login.png")
raiz.geometry("1200x600")
raiz.config(bg="black")

miFrame=Frame()
miFrame.pack(fill="both", expand="true")
miFrame.config(bg="grey")
miFrame.config(width="650", height="350")
miFrame.config(bd=35) #grosor del borde en 3d
miFrame.config(relief="solid")
miFrame.config(cursor="hand2")

milabel=Label(miFrame, text="sistema para calcular elpeso de barras", fg="black")
milabel.place(x=10, y=10)
milabel.config(bg="grey")



raiz.mainloop()
