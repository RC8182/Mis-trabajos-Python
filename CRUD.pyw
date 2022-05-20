
from Modulos.funciones import*



root=Tk()
root.grid()
root.title("My First CRUD")

valorRadio=IntVar()
frame=Frame(root)
frame1=Frame(root)
frame2=Frame(root)
frame3=Frame(root)



#------------------MENU----------------------------#
menuBar=Menu(root) # 1 Creamos Menu 
root.config(menu=menuBar) # 2 Le decimos a root que hemos creado un meni

menuArchivo=Menu(menuBar,tearoff=0) # 3 Creamos el primer elemento del menu
menuBar.add_cascade(label="Archivo", menu=menuArchivo) # 4 Damos nombre al primer elemento del menu
menuArchivo.add_command(label="Conectar DDBB",command=lambda:conectarBBDD())
menuArchivo.add_command(label="Desconectar DDBB", command=lambda:desconectarBBDD)
menuArchivo.add_command(label="Salir", command=lambda:salirDelPrograma(root))

menuLimpiar=Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Limpiar", menu=menuLimpiar)
menuLimpiar.add_command(label="Limpiar Campos", command=lambda:limpiarCampos())

menuAyuda=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Licencia", command=lambda:licencia())

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miTelefono=StringVar()
miTexto=StringVar()

def eliminar():
    miConexion=sqlite3.connect("Proyectos\CRUD\Almacenamiento\MiPrimerDB") # 1 Creamos y abrimos la BBDD
    miPuntero= miConexion.cursor()           # 2 Creamos el cursor
    miPuntero.execute("DELETE FROM AGENDA  WHERE ID="+ miId.get())
    miConexion.commit() # 3Confirmamos los cambios que hemos hecho en la tabla 
    messagebox.showinfo("BBDD", "Registro ELIMINADO con exito!")

def actualizar():
    miConexion=sqlite3.connect("Proyectos\CRUD\Almacenamiento\MiPrimerDB") # 1 Creamos y abrimos la BBDD
    miPuntero= miConexion.cursor()           # 2 Creamos el cursor
    listaDatos=[miNombre.get(),miApellido.get(),miTelefono.get()]
    miPuntero.execute("UPDATE AGENDA SET NOMRE_PERSONA=?, APELLIDO_PERSONA=?, TELEFONO_PERSONA=? WHERE ID="+ miId.get(), listaDatos)
    miConexion.commit() # 3Confirmamos los cambios que hemos hecho en la tabla 
    messagebox.showinfo("BBDD", "Registro Actualizado con exito!")

def leerBBDD():

    miConexion=sqlite3.connect("Proyectos\CRUD\Almacenamiento\MiPrimerDB") # 1 Creamos y abrimos la BBDD
    miPuntero= miConexion.cursor()           # 2 Creamos el cursor
    try:

        miPuntero.execute("SELECT * FROM AGENDA WHERE ID=" + miId.get())
        agenda=miPuntero.fetchall()

        for i in agenda:
            a=f"Nombre: {i[1]} Apellido: {i[2]} Numero de telefono: {i[3]}"
            print(a)
            miNombre.set(i[1])
            miApellido.set(i[2])
            miTelefono.set(i[3])

            messagebox.showinfo("BBDD", "Lectura Correcta")
    except:
            messagebox.showwarning("BBDD", "Lectura incorrecta, rellena el campo ID")        
        
    miConexion.commit()
      

def limpiarCampos():
    miId.set(" ")
    miNombre.set(" ")
    miApellido.set(" ")
    miTelefono.set(" ")
    

def pintarInterface():

    if valorRadio.get()==1:  #Create
        frame3.grid_forget()
        frame2.grid_forget()
        frame1.grid_forget()
        frame.grid()

        Label(frame,text="Nombre").grid(row=2, column=0)
        nombre=Entry(frame, textvariable=miNombre)
        nombre.grid(row=2, column=1)
        Label(frame,text="Apellido").grid(row=3, column=0)
        apellido=Entry(frame, textvariable=miApellido)
        apellido.grid(row=3, column=1)
        Label(frame,text="Telefono").grid(row=4, column=0)
        telefono=Entry(frame, textvariable= miTelefono)
        telefono.grid(row=4, column=1)
        Button(frame, text="Create", command=lambda:agregatPersona(nombre.get(),apellido.get(),telefono.get())).grid(row=5, column=2,columnspan=3,sticky="we")
           


    if valorRadio.get()==2: # Read
        frame3.grid_forget()
        frame2.grid_forget()
        frame.grid_forget()
        frame1.grid()
        Label(frame1,text="ID").grid(row=1, column=0)
        numero=Entry(frame1, textvariable=miId)
        numero.grid(row=1, column=1)
        Label(frame1,text="Nombre").grid(row=2, column=0)
        nombre=Entry(frame1, textvariable=miNombre)
        nombre.grid(row=2, column=1)
        Label(frame1,text="Apellido").grid(row=3, column=0)
        apellido=Entry(frame1, textvariable=miApellido)
        apellido.grid(row=3, column=1)
        Label(frame1,text="Telefono").grid(row=4, column=0)
        telefono=Entry(frame1, textvariable=miTelefono)
        telefono.grid(row=4, column=1)

        Button(frame1, text="Read", command=lambda:leerBBDD()).grid(row=5, column=2,columnspan=3,sticky="we") 
        '''textoComentario=Text(frame1,width=16, height=5)
        textoComentario.grid(row=1, column=2, sticky="we")
        scroltext=Scrollbar(frame1,command=textoComentario.yview)
        scroltext.grid(row=1, column=3)
        textoComentario.config(yscrollcommand=scroltext.set)'''


    if valorRadio.get()==3: # Update
        frame3.grid_forget()
        frame.grid_forget()
        frame1.grid_forget()
        frame2.grid()   

        Label(frame2,text="Nombre").grid(row=2, column=0)
        nombre=Entry(frame2, textvariable=miNombre)
        nombre.grid(row=2, column=1)
        Label(frame2,text="Apellido").grid(row=3, column=0)
        apellido=Entry(frame2, textvariable=miApellido)
        apellido.grid(row=3, column=1)
        Label(frame2,text="Telefono").grid(row=4, column=0)
        telefono=Entry(frame2, textvariable=miTelefono)
        telefono.grid(row=4, column=1)
        Button(frame2, text="Update",command=lambda:actualizar()).grid(row=5, column=2,columnspan=3,sticky="we")

    if valorRadio.get()==4: # Delete
        frame.grid_forget()
        frame2.grid_forget()
        frame1.grid_forget()
        frame3.grid()        

        Label(frame3,text="ID").grid(row=1, column=0)
        numero=Entry(frame3, textvariable=miId)
        numero.grid(row=1, column=1)
        Label(frame3,text="Nombre").grid(row=2, column=0)
        nombre=Entry(frame3, textvariable=miNombre)
        nombre.grid(row=2, column=1)
        Label(frame3,text="Apellido").grid(row=3, column=0)
        apellido=Entry(frame3, textvariable=miApellido)
        apellido.grid(row=3, column=1)
        Button(frame3, text="Delete",command=lambda:eliminar()).grid(row=5, column=2,columnspan=3,sticky="we")   
        


c=Radiobutton(root,text="Create",value=1, variable=valorRadio, command=pintarInterface)
c.grid(row=0,column=0, sticky="e")
r=Radiobutton(root,text="Read",value=2, variable=valorRadio, command=pintarInterface)
r.grid(row=0,column=1)
u=Radiobutton(root,text="Update",value=3, variable=valorRadio, command=pintarInterface)
u.grid(row=0,column=2)
d=Radiobutton(root,text="Delete",value=4, variable=valorRadio, command=pintarInterface)
d.grid(row=0,column=3)

 

root.mainloop()