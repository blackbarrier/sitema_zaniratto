from logging.config import valid_ident
from struct import pack
import tkinter as tk
from tkinter import ttk

   #Creo la ventana
ventana2 = tk.Tk()
ventana2.title("modificacion")
ventana2.geometry("600x300")

    #Creo los titulos y boton
titulo=tk.Label(ventana2, text="Menu 'Modificar Alumno' ", )
titulo2=tk.Label(ventana2, text="Seleccione alumno a modificar", )
btn1=tk.Button(ventana2,text="Modificar", )

    #Creo la Tabla
tree = ttk.Treeview(ventana2)
tree['columns'] = ("Nombre", "Apellido", "Carrera")
tree.column("#0", width=0, stretch=0)
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido", )
tree.heading("Carrera", text="Carrera")

    #Meto los datos
tree.insert(parent="", index=1,values=("Leandro","Barrera",26))


    #Ubico los elementos con el metodo "pack"
titulo.pack()
titulo2.pack()
tree.pack()
btn1.pack()

ventana2.mainloop()