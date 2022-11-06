from enum import Flag
from json.tool import main
from smtplib import OLDSTYLE_AUTH
import sqlite3 as sql
from tkinter.tix import INTEGER
from tokenize import String

# crear base de datos
def creardb():
    con=sql.connect("colegio.db")
    con.commit()
    con.close()

# crear tabla
def create_table():
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    cursor.execute("""CREATE TABLE if not exists
    ALUMNO(id_alumno integer primary key autoincrement,
    nombre text,
    apellido text,
    carrera text)""")
    cursor.execute("""CREATE TABLE if not exists
    NOTAS  (id_nota integer primary key autoincrement,
    id_alumno integer,
    nota integer,    
    foreign key ("id_alumno") references "ALUMNO" ("id_alumno")) """)
    con.commit()
    con.close()

 # crear alumno
def create_alumn():
    nombre= input("Ingrese nombre: ")
    apellido= input("Ingrese apellido: ")
    carrera= input("ingrese carrera: ")
    if not nombre or not apellido or not carrera:
        print("Cargue todos los datos.")
    else:      
        con=sql.connect("colegio.db")
        cursor=con.cursor()
        S=("""INSERT INTO ALUMNO (nombre,apellido,carrera) 
        VALUES (?,?,?)""") 
        cursor.execute(S,[nombre,apellido,carrera])
        print("Alumno creado con exito")  
        con.commit()
        con.close()
    
        
        
  # consulta los alumnos en la base de datos  
def consulta():
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    cursor.execute("""SELECT * FROM ALUMNO""")
    for i in cursor:
        print(i)
    con.commit()
    con.close()

  #busca un alumno en la base de datos
def buscar():
    opcion=input("Desea buscar por ID o nombre y apellido? ID/NA: ")
    
    if opcion=="ID":
        id_buscada=input("Ingrese ID a buscar: ")
        if not id_buscada:
            print("Debe seleccionar ingresar un ID en formato numerico")
        else:
            con=sql.connect("colegio.db")
            cursor=con.cursor()
            cursor.execute("SELECT * FROM ALUMNO where id_alumno="+str(id_buscada))
            flag = True
            for i in cursor:
                flag=False
                print (i)
            con.close()
            if flag:
                print("No se encontro")

    elif opcion=="NA":
        nombre_buscado=input("Ingrese nombre a buscar o *: ")
        apellido_buscado=input("Ingrese apellido a buscar o *: ")
       
        if not nombre_buscado or not apellido_buscado:
            print("Debe completar todos los campos")
        
        else:
            flag = True

            if apellido_buscado=="*" and nombre_buscado=="*":
                consulta()

            elif nombre_buscado=="*" and apellido_buscado!="*":
                con=sql.connect("colegio.db")
                cursor=con.cursor()
                cursor.execute("SELECT * FROM ALUMNO where apellido="+"'"+apellido_buscado+"'")
                for i in cursor:
                    flag=False
                    print(i)
                con.close()
                if flag:
                    print("No se encontro")

            elif apellido_buscado=="*" and nombre_buscado!="*":
                con=sql.connect("colegio.db")
                cursor=con.cursor()
                cursor.execute("SELECT * FROM ALUMNO where nombre="+"'"+nombre_buscado+"'")
                for i in cursor:
                    flag=False
                    print(i)
                con.close()
                if flag:
                    print("No se encontro")

            else:
                con=sql.connect("colegio.db")
                cursor=con.cursor()
                cursor.execute("SELECT * FROM ALUMNO where nombre="+"'"+nombre_buscado+"'")
                for i in cursor:
                    if i[2]==apellido_buscado:
                        flag=False
                        print (i)    
                if flag:
                    print("No se encontro al alumno.")           
    else:
        print("Debe seleccionar una opcion valida")
 

def borrar():
    id_buscada=input("Ingrese id de alumno a eliminar: ")
   
    con=sql.connect("colegio.db")
    cursor=con.cursor()
    cursor.execute("DELETE FROM ALUMNO where id_alumno="+"'"+id_buscada+"'")
    con.commit()
    con.close()
    print("Se borro el alumno.")
    consulta()

def modificar():
    Flag = True
    id_alumno=int(input("Ingrese legajo de alumno a modificar: "))    
    con=sql.connect("colegio.db")
    cursor=con.cursor()   
    cursor.execute("SELECT * FROM ALUMNO where id_alumno="+str(id_alumno))
    for i in cursor:
        print(i)
        Flag = False
        print("Modificar nombre o apellido?: ")              
        opcion=int(input("Nombre [1] / Apellido [2]: "))
        nuevo=input("Ingrese nuevo nombre/apellido: ")
        if opcion == 1:
            cursor.execute("UPDATE ALUMNO set nombre=" + "'" + nuevo + "'" + "where id_alumno="+str(id_alumno))
            print("Alumno modificado con exito")
        
        elif opcion==2:
            cursor.execute("UPDATE ALUMNO set apellido=" + "'" + nuevo + "'" + "where id_alumno="+str(id_alumno))
            print("Alumno modificado con exito")

    con.commit()
    con.close()
    if Flag:
        print("Alumno no encontrado") 
    
    

def main():
    opcion=input('''Ingrese una opcion:
    1) Agregar alumno 
    2) Mostrar listado completo 
    3) Buscar 
    4) Borrar alumno
    5) Modificar
    0) Salir 
    ----------> ''')
    
    while opcion!=str(0):
        if opcion==str(1):
            create_alumn()
        elif opcion==str(2):
            consulta()
        elif opcion==str(3):
            print(buscar())
        elif opcion==str(4):
            borrar()
        elif opcion==str(5):
            modificar()
        else:
            print("Debe seleccionar una opcion valida.")

        opcion=input('''Ingrese una opcion:
        1) Agregar alumno 
        2) Mostrar listado completo 
        3) Buscar 
        4) Borrar alumno
        5) Modificar
        0) Salir 
        ----------> ''')       

    print("Finalizado")


creardb()
create_table()
main()


#pruebaa