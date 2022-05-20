from tkinter import messagebox
from tkinter import *
import sqlite3


def agregatPersona(nom,ape,tel):
    miConexion=sqlite3.connect("Proyectos\CRUD\Almacenamiento\MiPrimerDB") # 1 Creamos y abrimos la BBDD
    miPuntero= miConexion.cursor()           # 2 Creamos el cursor
    listaDatos=[nom,ape,tel]
    miPuntero.execute("INSERT INTO AGENDA VALUES(NULL,?,?,?)", listaDatos)
    miConexion.commit() # 3Confirmamos los cambios que hemos hecho en la tabla 
    messagebox.showinfo("BBDD", "Registro Creado con exito!")

def conectarBBDD():
    miConexion=sqlite3.connect("Proyectos\CRUD\Almacenamiento\MiPrimerDB") # 1 Creamos y abrimos la BBDD
    miPuntero= miConexion.cursor()           # 2 Creamos el cursor
    try:

        miPuntero.execute("CREATE TABLE  AGENDA(ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMRE_PERSONA VARCHAR(20), APELLIDO_PERSONA VARCHAR(20),TELEFONO_PERSONA INTEGER)")# 3 Creamos la tabla si no existe
        messagebox.showinfo("BBDD", "La base de datos ha sido creada con exito")
    except:
        messagebox.showwarning("Atencion!", "La BBDD ya ha sido creada")    


def desconectarBBDD():
    miConexion=sqlite3.connect("Proyectos\CRUD\Almacenamiento\MiPrimerDB")
    miConexion.close()


def salirDelPrograma(r):
    x=messagebox.askquestion("Salir","Realmente deceas salir del Programa")
    if x == "yes":
        r.destroy()

def licencia():
    messagebox.showwarning("Licencia", "Licencia GNU @Javier Visconti") # Agregamos los parametros y llamaremos a la funcion al clickear Licencia


     



    





