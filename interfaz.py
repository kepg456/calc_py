from ast import For
from cgitb import text
from tkinter import *
from tkinter.font import BOLD


ventana = Tk()
ventana.title("calculadora")
ventana.config(width=550,height=550,background="#614C47")
ventana.maxsize(550, 500)
ventana.minsize(550,500)

caja = Text(width=23, height=2,font=("Courier",30,BOLD))
caja.place(x=0,y=0)

"""esta es la parte de las teclas de los numeros"""

"""definicion de la funcion de los botones"""
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
""" aca terminan las teclas de los numeros"""
ventana.mainloop()