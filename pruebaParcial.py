from cProfile import label
from cgitb import text
from operator import truediv
from tkinter import *
import tkinter
from webbrowser import get



def imprimir(): 
    print(lista)

def cargar_lista(lista):
    valor=int(edit1.get())
    lista.append(valor)
    imprimir(lista)

def remover(lista):        
    valor=int(edit1.get())
    if (valor in lista):
        lista.remove(valor)
        imprimir(lista)
    else:
        print("Valor no encontrado")


lista=[1,2,3,4]
l2=[7,8,9,0]


#Elementos Tkinter
ventana =tkinter.Tk()
ventana.title("Ventana de practica")
ventana.geometry("400x300")

etiqueta1=tkinter.Label(ventana, text="Holaa",)

edit1=tkinter.Entry(ventana)


boton_cargar=tkinter.Button(ventana, text="Cargar dato",command=cargar_lista)
boton_imprimir=tkinter.Button(ventana, text="Imprimir lista por consola",command=imprimir)
boton_remover=tkinter.Button(ventana, text="Eliminar elemento", command=remover)

#Posicion
etiqueta1.pack()
edit1.pack()
boton_cargar.pack()
boton_imprimir.pack()
boton_remover.pack()
ventana.mainloop()








