from ast import For
from tkinter import *
from tkinter.font import BOLD


ventana = Tk()
ventana.title("calculadora")
ventana.config(width=550,height=550,background="white")


def click_boton():
    texto = Label(text="boton presionado hijo de puta")
    texto.place(x=0,y=0)
xf=80
yf=120
filas=0
for i in range(10):
    i=i+1
    boton = Button(text=i-1,height=3,width=6,font=("Courier",13,BOLD),command=click_boton)
    boton.place(x=xf,y=yf)
    xf= xf + 100
    if(xf>300):
        filas = filas + 1 
        xf=80
        if(filas == 3):
            xf = xf + 100
            yf=yf+100
        else:
            yf=yf+100

ventana.mainloop()