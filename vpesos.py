from tkinter import *
from PIL import *
from tkinter import PhotoImage

ventana_p = Tk()
ventana_p.title('login')
#ventana_p.minsize(width=500, height=600)
ventana_p.geometry("1200x600")
ventana_p.resizable(False, False )
ventana_p.config(padx=35,pady=35)
ventana_p.config(bg="green")

#aca colocaremos una imagen
#'''f_logo = PhotoImage(file="login.png")
canv_logo = Canvas(width=256, height=256)
#canv_logo.create_image(100, 100, Image= PhotoImage(file="login.png"))
canv_logo.grid(column=0, row=0)
#**************************************************
e_usuario = Label(text='Usuario : ', font=('Arial', 12))
e_usuario.grid(column=0, row=1)

c_usuario = Entry(width=20,font=('arial',12))
c_usuario.grid(column=1, row=1)
c_usuario.config(bg="blue")

e_pasw = Label(text='Contraseña: ', font=('Arial', 12))
e_pasw.grid(column=0, row=3)

c_pasw = Entry(width=20,font=('arial',12))
c_pasw.grid(column=1, row=3)

b_login = Button(text='aceptar', font=('Arial', 12))
b_login.grid(column=0, row=7)

b_cancel = Button(text='Cancelar', font=('Arial', 12))
b_cancel.grid(column=1, row=7)

miFrame=Frame()


ventana_p.mainloop()