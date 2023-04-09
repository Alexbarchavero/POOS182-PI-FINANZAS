from tkinter import ttk, Tk, Toplevel, Frame, StringVar, BOTH, Label, Entry, Button, OptionMenu, END, BOTTOM
from tkinter import *
from usuarios import *
import datetime

# Creamos la ventana 1 centrada
w1 = Tk()
w1.title("Inicio")
ancho1 = w1.winfo_screenwidth()
alto1 = w1.winfo_screenheight()
w1_ancho = 1120
w1_alto = 480
x = int((ancho1-w1_ancho)/2)
y = int((alto1-w1_alto)/2)
w1.geometry("{}x{}+{}+{}".format(w1_ancho,w1_alto,x,y))
# Creamos el Notebook para la ventana 1
panel1 = ttk.Notebook(w1)
panel1.pack(fill = BOTH, expand = True)
p1_1 = Frame(panel1)
p1_2 = Frame(panel1)
p1_3 = Frame(panel1)
p1_4 = Frame(panel1)
# Nombramos las pestañas en el panel
panel1.add(p1_1, text = "Registrarse")
panel1.add(p1_2, text = "Iniciar Sesion")
panel1.add(p1_3, text = "Actualizar Datos")
panel1.add(p1_4, text = "Eliminar Cuenta")

# Creamos la ventana 2 centrada
w2 = Toplevel(w1)
w2.title("Finanzas")
ancho2 = w2.winfo_screenwidth()
alto2 = w2.winfo_screenheight()
w2_ancho = 1120
w2_alto = 480
x = int((ancho2-w2_ancho)/2)
y = int((alto2-w2_alto)/2)
w2.geometry("{}x{}+{}+{}".format(w2_ancho,w2_alto,x,y))
# Creamos el Notebook para la ventana 2
panel2 = ttk.Notebook(w2)
panel2.pack(fill = BOTH, expand = True)
# Añadimos las pestañas al panel 2
p2_1 = Frame(panel2)
p2_2 = Frame(panel2)
p2_3 = Frame(panel2)
p2_4 = Frame(panel2)
p2_5 = Frame(panel2)
p2_6 = Frame(panel2)
# Nombramos las pestañas en el panel
panel2.add(p2_1, text = "Ingreso")
panel2.add(p2_2, text = "Gasto")
panel2.add(p2_3, text = "Compra")
panel2.add(p2_4, text = "Pago")
panel2.add(p2_5, text = "Consultar Registros")
panel2.add(p2_6, text = "Cerrar sesion")
# Ocultamos de inicio la ventana 2
w2.withdraw()

# Variables
name = StringVar()
password = StringVar()
nocuenta = StringVar()

nombre = StringVar()
contra = StringVar()
cuenta = StringVar()
categoria = StringVar()
tipo = StringVar()
descripcion = StringVar()
monto = StringVar()

# Instancia
exe = usuarios(nombre,contra,cuenta,categoria,tipo,descripcion,monto)

# -------------------------------------------------- Metodo para la fecha actual -------------------------------------------------- #
def actualizar_fecha(label):
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime('%d/%m/%Y %H:%M:%S')
    label.config(text=fecha_formateada)
    label.after(1000, actualizar_fecha, label)

# -------------------------------------------------- Metodos de pestaña 1 -------------------------------------------------- #

# Metodo: ejecutar registrar usuario
def exeSignUp():
    exe.signup()
    ENnombre1.delete(0, END)
    ENcontra1.delete(0, END)
    ENcuenta1.delete(0, END)

# Metodo: ejecutar iniciar sesion
def exeLogin():
    r = exe.login()
    ENnombre2.delete(0, END)
    ENcontra2.delete(0, END)
    if r==True:
        w1.withdraw()
        w2.deiconify()

# Metodo: ejecutar actualizar info
def exeUpdateInfo():
    if name.get() and password.get() and nocuenta.get():
        exe.updateInfo(name.get(), password.get(), nocuenta.get())
    else:
        messagebox.showwarning("Advertencia", "Los campos Nuevo Nombre y Nueva Contraseña son requeridos.")
    ENnombre3.delete(0,END)
    ENcontra3.delete(0,END)
    ENname1.delete(0,END)
    ENpass1.delete(0,END)
    ENcuenta2.delete(0,END)

# Metodo: ejecutar eliminar usuario
def deleteUser():
    exe.deleteAccount()
    ENnombre4.delete(0,END)
    ENcontra4.delete(0,END)

# -------------------------------------------------- Metodos de pestaña 2 -------------------------------------------------- #

# Metodo: ejecutar añadir transaccion
def exeAddTransaccion():
    index = panel2.index(panel2.select())
    if index==0:
        categoria = "Ingreso"
        exe.addTransaccion(categoria)
        ENdescripcion1.delete(0,END)
        ENmonto1.delete(0,END)
    elif index==1:
        categoria = "Gasto"
        ENdescripcion2.delete(0,END)
        ENmonto2.delete(0,END)
        exe.addTransaccion(categoria)
    elif index==2:
        categoria = "Compra"
        ENdescripcion3.delete(0,END)
        ENmonto3.delete(0,END)
        exe.addTransaccion(categoria)
    elif index==3:
        categoria = "Pago"
        ENdescripcion4.delete(0,END)
        ENmonto4.delete(0,END)
        exe.addTransaccion(categoria)
    tipo.set("Seleccionar")

# Metodo: ejecutar mostrar transacciones
def exeShowTransacciones():
    tvTransacciones.delete(*tvTransacciones.get_children())
    registros = exe.showTransacciones()
    if registros:
        for i in registros:
            cadena = (i[0],i[1],i[2],i[3],i[4],i[5])
            tvTransacciones.insert("",END,values=cadena)
    else:
        messagebox.showinfo("Datos inexistentes","No hay registros para mostrar")

# Metodo: ejecutar cerrar sesion
def exeLogout():
    exe.logout()
    w2.destroy()
    w1.deiconify()
    
# -------------------------------------------------- Widgets de pestaña 1 -------------------------------------------------- #

# Widgets ventana 1, pestaña 1
titulo1 = Label(p1_1,text="Registrarse",fg="green",font=("Century Gothic",16))
titulo1.pack()

LBnombre1 = Label(p1_1,text="Ingrese su Nombre: ",font=("Century Gothic",12))
LBnombre1.pack()
ENnombre1 = Entry(p1_1,textvariable=nombre)
ENnombre1.pack()

LBcontra1 = Label(p1_1,text="Ingrese una Contraseña: ",font=("Century Gothic",12))
LBcontra1.pack()
ENcontra1 = Entry(p1_1,textvariable=contra)
ENcontra1.pack()

LBcuenta1 = Label(p1_1,text="Ingrese un numero de cuenta de banco: ",font=("Century Gothic",12))
LBcuenta1.pack()
ENcuenta1 = Entry(p1_1,textvariable=cuenta)
ENcuenta1.pack()

btnRegistro = Button(p1_1,text="Registrar",font=("Century Gothic",12),bg="light blue",command=exeSignUp)
btnRegistro.pack()

label_fecha1 = Label(p1_1, font=('Century Gothic', 12))
label_fecha1.pack(side=BOTTOM,fill=BOTH,expand=True)
actualizar_fecha(label_fecha1)

# Widgets ventana 1, pestaña 2
titulo2 = Label(p1_2,text="Iniciar Sesion",fg="green",font=("Century Gothic",16))
titulo2.pack()

LBnombre2 = Label(p1_2,text="Ingrese su Nombre: ",font=("Century Gothic",12))
LBnombre2.pack()
ENnombre2 = Entry(p1_2,textvariable=nombre)
ENnombre2.pack()

LBcontra2 = Label(p1_2,text="Ingrese su Contraseña: ",font=("Century Gothic",12))
LBcontra2.pack()
ENcontra2 = Entry(p1_2,textvariable=contra,show="*")
ENcontra2.pack()

btnIngreso = Button(p1_2,text="Ingresar",font=("Century Gothic",12),bg="light green",command=exeLogin)
btnIngreso.pack()

label_fecha2 = Label(p1_2, font=('Century Gothic', 12))
label_fecha2.pack(side=BOTTOM,fill=BOTH,expand=True)
actualizar_fecha(label_fecha2)

# Widgets Ventana 1 Pestaña 3
titulo3 = Label(p1_3,text="Actualizar informacion de la cuenta",fg="green",font=("Century Gothic",16))
titulo3.pack()

LBnombre3 = Label(p1_3,text="Nombre:",font=("Century Gothic",12))
LBnombre3.pack()
ENnombre3 = Entry(p1_3,textvariable=nombre)
ENnombre3.pack()
LBcontra3 = Label(p1_3,text="Contraseña:",font=("Century Gothic",12))
LBcontra3.pack()
ENcontra3 = Entry(p1_3,textvariable=contra,show="*")
ENcontra3.pack()

LBname1 = Label(p1_3,text="Nuevo nombre:",font=("Century Gothic",12))
LBname1.pack()
ENname1 = Entry(p1_3,textvariable=name)
ENname1.pack()
LBpass1 = Label(p1_3,text="Nueva contraseña:",font=("Century Gothic",12))
LBpass1.pack()
ENpass1 = Entry(p1_3,textvariable=password)
ENpass1.pack()
LBcuenta2 = Label(p1_3,text="Nuevo numero de cuenta:",font=("Century Gothic",12))
LBcuenta2.pack()
ENcuenta2 = Entry(p1_3,textvariable=nocuenta)
ENcuenta2.pack()

btnUpdate = Button(p1_3,text="Actualizar Informacion",font=("Century Gothic",12),command=exeUpdateInfo).pack()

label_fecha3 = Label(p1_3, font=('Century Gothic', 12))
label_fecha3.pack(side=BOTTOM,fill=BOTH,expand=True)
actualizar_fecha(label_fecha3)

# Widgets Ventana 1 Pestaña 4
titulo4 = Label(p1_4,text="Eliminar cuenta",fg="green",font=("Century Gothic",16))
titulo4.pack()

LBnombre4 = Label(p1_4,text="Nombre:",font=("Century Gothic",12))
LBnombre4.pack()
ENnombre4 = Entry(p1_4,textvariable=nombre)
ENnombre4.pack()
LBcontra4 = Label(p1_4,text="Contraseña:",font=("Century Gothic",12))
LBcontra4.pack()
ENcontra4 = Entry(p1_4,textvariable=contra)
ENcontra4.pack()

btnDeleteAccount = Button(p1_4,text="Eliminar Cuenta",font=("Century Gothic",12),command=deleteUser).pack()

label_fecha4 = Label(p1_4, font=('Century Gothic', 12))
label_fecha4.pack(side=BOTTOM,fill=BOTH,expand=True)
actualizar_fecha(label_fecha4)

# -------------------------------------------------- Widgets de pestaña 2 -------------------------------------------------- #

# Widgets ventana 2, pestaña 1
titu1 = Label(p2_1,text="Ingresos",fg="green",font=("Century Gothic",16))
titu1.pack()
LBtipo1 = Label(p2_1, text="Tipo:",font=("Century Gothic",12))
LBtipo1.pack()
tipo.set("Seleccionar")
OMtipo1 = OptionMenu(p2_1, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito")
OMtipo1.pack()
LBdescripcion1 = Label(p2_1, text="Descripción:",font=("Century Gothic",12))
LBdescripcion1.pack()
ENdescripcion1 = Entry(p2_1,textvariable=descripcion)
ENdescripcion1.pack()
LBmonto1 = Label(p2_1, text="Monto:",font=("Century Gothic",12))
LBmonto1.pack()
ENmonto1 = Entry(p2_1,textvariable=monto)
ENmonto1.pack()

btnAddRegistro1 = Button(p2_1,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

# Widgets ventana 2, pestaña 2
titu2 = Label(p2_2,text="Gastos",fg="green",font=("Century Gothic",16))
titu2.pack()
LBtipo2 = Label(p2_2, text="Tipo:",font=("Century Gothic",12))
LBtipo2.pack()
tipo.set("Seleccionar")
OMtipo2 = OptionMenu(p2_2, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito")
OMtipo2.pack()
LBdescripcion2 = Label(p2_2, text="Descripción:",font=("Century Gothic",12))
LBdescripcion2.pack()
ENdescripcion2 = Entry(p2_2,textvariable=descripcion)
ENdescripcion2.pack()
LBmonto2 = Label(p2_2, text="Monto:",font=("Century Gothic",12))
LBmonto2.pack()
ENmonto2 = Entry(p2_2,textvariable=monto)
ENmonto2.pack()

btnAddRegistro2 = Button(p2_2,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

# Widgets ventana 2, pestaña 3
titu3 = Label(p2_3,text="Compras",fg="green",font=("Century Gothic",16))
titu3.pack()
LBtipo3 = Label(p2_3, text="Tipo:",font=("Century Gothic",12))
LBtipo3.pack()
tipo.set("Seleccionar")
OMtipo3 = OptionMenu(p2_3, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito")
OMtipo3.pack()
LBdescripcion3 = Label(p2_3, text="Descripción:",font=("Century Gothic",12))
LBdescripcion3.pack()
ENdescripcion3 = Entry(p2_3,textvariable=descripcion)
ENdescripcion3.pack()
LBmonto3 = Label(p2_3, text="Monto:",font=("Century Gothic",12))
LBmonto3.pack()
ENmonto3 = Entry(p2_3,textvariable=monto)
ENmonto3.pack()

btnAddRegistro3 = Button(p2_3,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

# Widgets ventana 2, pestaña 4
titu4 = Label(p2_4,text="Pagos",fg="green",font=("Century Gothic",16))
titu4.pack()
LBtipo4 = Label(p2_4, text="Tipo:",font=("Century Gothic",12))
LBtipo4.pack()
tipo.set("Seleccionar")
OMtipo4 = OptionMenu(p2_4, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito")
OMtipo4.pack()
LBdescripcion4 = Label(p2_4, text="Descripción:",font=("Century Gothic",12))
LBdescripcion4.pack()
ENdescripcion4 = Entry(p2_4,textvariable=descripcion)
ENdescripcion4.pack()
LBmonto4 = Label(p2_4, text="Monto:",font=("Century Gothic",12))
LBmonto4.pack()
ENmonto4 = Entry(p2_4,textvariable=monto)
ENmonto4.pack()

btnAddRegistro4 = Button(p2_4,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

#Widgets Ventana 2 Pestaña 5
titu5 = Label(p2_5,text="Consultar Registros",fg="green",font=("Century Gothic",16)).pack()
btnConsultar = Button(p2_5,text="Consultar",font=("Century Gothic",16),command=exeShowTransacciones).pack()
tvTransacciones = ttk.Treeview(p2_5,columns=('id','categoria','tipo','descripcion','monto','usuario_id'),show="headings")
tvTransacciones.heading('#0',text="Index")
tvTransacciones.heading('id',text="Id")
tvTransacciones.heading('categoria',text="Categoria")
tvTransacciones.heading('tipo',text="Tipo")
tvTransacciones.heading('descripcion',text="Descripcion")
tvTransacciones.heading('monto',text="Monto")
tvTransacciones.heading('usuario_id',text="Id de Usuario")
tvTransacciones.pack(expand=True, fill=BOTH)

# Widgets Ventana 2 Pestaña 6
titu6 = Label(p2_6,text="Cerrar Sesion",fg="green",font=("Century Gothic",16)).pack()
btnCloseSesion = Button(p2_6,text="Cerrar Sesion",font=("Century Gothic",12),command=exeLogout).pack()

# -------------------------------------------------- MAINLOOP -------------------------------------------------- #
w1.mainloop()