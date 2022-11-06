import tkinter

def cargar_nota(valor):
    nota=int(valor.get())
    notas.append(nota)
    return

def sig_alumno():
    listado.append(notas)
    print(listado)
    return

def exit():
    ventana.quit()
    return

listado=[]
notas=[]

ventana = tkinter.Tk()
ventana.geometry("400x300")
ventana.title("Carga de notas")

edit1=tkinter.Entry(ventana)
btn_cargar=tkinter.Button(ventana, text="Cargar nota", command=cargar_nota)
btn_salir=tkinter.Button(ventana, text="Salir", command=exit)
btn_siguiente=tkinter.Button(ventana, text="Siguiente", command=sig_alumno)
titulo=tkinter.Label(ventana, text="Ingrese las notas por alumno")


titulo.pack()
edit1.pack()
btn_cargar.pack()
btn_siguiente.pack()
btn_salir.pack()

ventana.mainloop()