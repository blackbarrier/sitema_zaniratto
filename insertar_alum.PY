import tkinter
import sqlite3 as sql
from tkinter import messagebox



def create_alumn():
    nombre=input1.get()
    apellido=input2.get()
    carrera=input3.get()
        

    if not nombre or not apellido or not carrera:
        messagebox.showerror("Error","Complete todos los campos")
    else:      
        con=sql.connect("colegio.db")
        cursor=con.cursor()
        S=("""INSERT INTO ALUMNO (nombre,apellido,carrera) 
        VALUES (?,?,?)""") 
        cursor.execute(S,[nombre,apellido,carrera])
        messagebox.showinfo("Info", "Alumno creado con exito") 
        con.commit()
        con.close()


     
ventana = tkinter.Tk()
ventana.geometry("500x500")

titulo=tkinter.Label(ventana, text="Menu 'Agregar Alumno' ", )
label1=tkinter.Label(ventana, text="Ingrese nombre: ", )
label2=tkinter.Label(ventana, text="Ingrese apellido: ",)
label3=tkinter.Label(ventana, text="Ingrese carrera: ",)

nombre=tkinter.StringVar()
apellido=tkinter.StringVar()
carrera=tkinter.StringVar()


input1=tkinter.Entry(ventana, textvariable=nombre)
input2=tkinter.Entry(ventana, textvariable=apellido)
input3=tkinter.Entry(ventana, textvariable=carrera)

btn1=tkinter.Button(ventana,text="Agregar alumno", command=create_alumn)



titulo.pack()
label1.pack()
input1.pack()
label2.pack()
input2.pack()
label3.pack()
input3.pack()
btn1.pack()


ventana.mainloop()