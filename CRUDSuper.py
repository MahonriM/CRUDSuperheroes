from tkinter import *
from tkinter import messagebox
import sqlite3
def conexionBBDD():
    miConexion= sqlite3.connect("Super")
    micursor= miConexion.cursor()
    try:
        micursor.execute('''Create Table super(ID Integer primary key autoincrement,Nombre varchar(50),
        Sexo char(2),Poder varchar(50))''')
        messagebox.showinfo("BBDD","Base de datos creado")
    except:
        messagebox.showwarning("ATENCION","La base de datos ya ha sido creado")
def salir():
    valor=messagebox.showwarning("¡ATENCION!","Deseas salir")
    if valor == "yes":
        root.destroy()
def limpiar():
    miID.set("")
    miNombre.set("")
    miPoder.set("")
    miSexo.set("")
def eliminar():
    try:
        miConexion=sqlite3.connect("Super")
        micursor=miConexion.cursor()
        micursor.execute("Delete From super where ID="+ miID.get())
    except:
        messagebox.showinfo("BBDD","Ha ocurrido un error")
def leer():
    miConexion =sqlite3.connect("Super")
    micursor=miConexion.cursor()
    micursor.execute("Select * From super where ID="+ miID.get())
    super=micursor.fetchall()
    for Super in super:
        miID.set(Super[0])
        miNombre.set(Super[1])
        miSexo.set(Super[2])
        miPoder.set(Super[3])
        miConexion.commit()
    
def insertar():
    miConexion=sqlite3.connect("Super")
    micursor=miConexion.cursor()
    micursor.execute("INSERT INTO super values(Null,?,?,?)",(
    miNombre.get(),miSexo.get(),miPoder.get()))
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro insertado con exito")
    #pass
def actualizar():
    miConexion=sqlite3.connect("Super")
    micursor=miConexion.cursor()
    micursor.execute("Update super set Nombre=?,Sexo=?,Poder=? where ID=?",(
    miNombre.get(),miSexo.get(),miPoder.get(),miID.get()))
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro Actualizado")
root=Tk()
root.title("Registro de superheroes")
root.iconbitmap("logo.ico")
barramenu=Menu(root)
root.config(menu=barramenu,width=300,height=300)
bbddmenu=Menu(barramenu,tearoff=0)
bbddmenu.add_command(label="Conectar",command=conexionBBDD)
bbddmenu.add_command(label="salir",command=salir)

borrarmenu=Menu(barramenu,tearoff=0)
borrarmenu.add_command(label="Borrar campos",command=limpiar)

crudMenu=Menu(barramenu,tearoff=0)
crudMenu.add_command(label="Crear",command=insertar)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Elimnar",command=eliminar)

barramenu.add_cascade(label="BBDD",menu=bbddmenu)
barramenu.add_cascade(label="Borrar",menu=borrarmenu)
barramenu.add_cascade(label="CRUD",menu=crudMenu)
miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miSexo=StringVar()
miPoder=StringVar()

CuadroID=Entry(miFrame,textvariable=miID)
CuadroID.grid(row=0,column=1,padx=10,pady=10)

CuadroNombre=Entry(miFrame,textvariable=miNombre)
CuadroNombre.grid(row=1,column=1,padx=10,pady=10)

CuadroSexo=Entry(miFrame,textvariable=miSexo)
CuadroSexo.grid(row=2,column=1,padx=10,pady=10)

CuadroPoder=Entry(miFrame,textvariable=miPoder)
CuadroPoder.grid(row=3,column=1,padx=10,pady=10)
#Labels
idlabel=Label(miFrame,text="ID:")
idlabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nomlabel=Label(miFrame,text="Nombre:")
nomlabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

sexolabel=Label(miFrame,text="Sexo:")
sexolabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

poderlabel=Label(miFrame,text="Poder:")
poderlabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)
#Botones
miFrame2=Frame(root)
miFrame2.pack()
botonCrear=Button(miFrame2,text="Crear",command=insertar)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonLeer=Button(miFrame2,text="Leer",command=leer)
botonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)

botonEliminar=Button(miFrame2,text="Eliminar",command=eliminar)
botonEliminar.grid(row=1,column=2,sticky="e",padx=10,pady=10)

botonActualizar=Button(miFrame2,text="Actualizar",command=actualizar)
botonActualizar.grid(row=1,column=3,sticky="e",padx=10,pady=10)
root.mainloop()