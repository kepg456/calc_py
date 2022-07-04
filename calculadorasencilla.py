from tkinter import *
from tkinter.font import BOLD

from interfaz import click_boton

i = 0
raiz = Tk()

caja2 = Entry(width=23,font=("Courier",30,BOLD))
caja2.grid(row=0,column=0,columnspan=4,padx=50,pady=5)

def click_boton2(valor):
    global i
    caja2.insert(i,valor)
    i+=1
Button(text="1",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(1)).grid(row=1,column=0)
Button(text="2",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(2)).grid(row=1,column=1)
Button(text="3",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(3)).grid(row=1,column=2)
Button(text="4",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(4)).grid(row=2,column=0)
Button(text="5",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(5)).grid(row=2,column=1)
Button(text="6",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(6)).grid(row=2,column=2)
Button(text="7",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(7)).grid(row=3,column=0)
Button(text="8",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(8)).grid(row=3,column=1)
Button(text="9",height=3,width=6,font=("Courier",13,BOLD),command= lambda: click_boton2(9)).grid(row=3,column=2)

raiz.mainloop()