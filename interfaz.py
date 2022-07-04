from ast import For
from cgitb import text
from tkinter import *
from tkinter.font import BOLD

lector=0
ventana = Tk()
ventana.title("calculadora")
ventana.config(width=550,height=550,background="#614C47")
ventana.maxsize(550, 500)
ventana.minsize(550,500)

"""caja = Text(width=23, height=2,font=("Courier",30,BOLD),state="disabled")
caja.place(x=0,y=0)
caja.insert(1,"hola")"""

caja1 = Entry(width=23,font=("Courier",30,BOLD))
caja1.place(x=0,y=0)

"""esta es la parte de las teclas de los numeros"""

"""definicion de la funcion de los botones"""
def click_boton(valor):
    global lector
    caja1.insert(lector,valor)
    lector = lector + 1

"""imprimir botones en la ventana"""
xf=80
yf=120
filas=0
numeros = []
u=0
for i in range(10):
    i=i+1
    numeros.append(Button(text=i-1,height=3,width=6,font=("Courier",13,BOLD)).place(x=xf,y=yf))
    u = u + 1
    xf= xf + 100
    if(xf>300):
        filas = filas + 1 
        xf=80
        if(filas == 3):
            xf = xf + 100
            yf=yf+100
        else:
            yf=yf+100

command= lambda x: print(x)


""" aca terminan las teclas de los numeros"""


def sumar():
    global lector
    caja1.insert(lector,"+")
    lector = lector + 1

photo = PhotoImage(file="suma.png")
photoimagen = photo.subsample(4,4)
boton_suma = Button(image= photoimagen,command=sumar)
boton_suma.place(x=400,y=300)


ventana.mainloop()