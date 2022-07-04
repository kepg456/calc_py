from tkinter import *

from setuptools import Command

raiz = Tk()
botones = []

def click(valor):
    texto = ("presionado ",valor)
    Label(text=texto).place(x=0,y=0)

for i in range(10):
    botones.append(Button(text="hola mundo",command = lambda: click(i)))





botones[3].place(y=40,x=0)

raiz.mainloop()