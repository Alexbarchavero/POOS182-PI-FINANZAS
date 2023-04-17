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
presupuesto = Frame(panel2)
p2_1 = Frame(panel2)
p2_2 = Frame(panel2)
p2_3 = Frame(panel2)
p2_4 = Frame(panel2)
p2_5 = Frame(panel2)
# Nombramos las pestañas en el panel
panel2.add(presupuesto, text = "Presupuesto")
panel2.add(p2_1, text = "Ingreso")
panel2.add(p2_2, text = "Egreso")
panel2.add(p2_3, text = "Impuestos")
panel2.add(p2_4, text = "Movimientos")
panel2.add(p2_5, text = "Cerrar sesion")
# Ocultamos de inicio la ventana 2
w2.withdraw()

# Variables
name = StringVar()
password = StringVar()
nocuenta = StringVar()
dinero = StringVar()
tipoIngreso = StringVar()
tipoEgreso = StringVar()

nombre = StringVar()
contra = StringVar()
cuenta = StringVar()
categoria = StringVar()
tipo = StringVar()
descripcion = StringVar()
monto = StringVar()

impuesto=0

# Instancia
exe = usuarios()

# -------------------------------------------------- Metodo para la fecha actual -------------------------------------------------- #
def actualizar_fecha(label):
    fecha_actual = datetime.datetime.now()
    fecha_formateada = fecha_actual.strftime('%d/%m/%Y %H:%M:%S')
    label.config(text=fecha_formateada)
    label.after(1000, actualizar_fecha, label)

# --------------------------------------------- Metodo para reiniciar la ventana 2 --------------------------------------------- #

def reset_w2():
    # Reiniciamos los valores de ENpresupuesto, labelPresupuesto, ENdescripcion1, ENmonto1, ENdescripcion2, ENmonto2 y LBimpuestos
    ENpresupuesto.delete(0, END)
    labelPresupuesto.config(text="Presupuesto $0.00")
    ENdescripcion1.delete(0, END)
    ENmonto1.delete(0, END)
    ENdescripcion2.delete(0, END)
    ENmonto2.delete(0, END)

    # Reiniciamos los valores del árbol de transacciones
    tvTransacciones.delete(*tvTransacciones.get_children())

# -------------------------------------------------- Metodos de pestaña 1 -------------------------------------------------- #

# Metodo: ejecutar registrar usuario
def exeSignUp():
    exe.signup(nombre.get(),contra.get(),cuenta.get())
    ENnombre1.delete(0, END)
    ENcontra1.delete(0, END)
    ENcuenta1.delete(0, END)

# Metodo: ejecutar iniciar sesion
def exeLogin():
    r = exe.login(nombre.get(),contra.get())
    ENnombre2.delete(0, END)
    ENcontra2.delete(0, END)
    if r==True:
        reset_w2()
        w2.deiconify()
        w1.withdraw()

# Metodo: ejecutar actualizar info
def exeUpdateInfo():
    if nombre.get() and contra.get() and name.get() and password.get() and nocuenta.get():
        exe.updateInfo(nombre.get(), contra.get(), name.get(), password.get(), nocuenta.get())
    else:
        messagebox.showwarning("Advertencia", "Los campos Nuevo Nombre y Nueva Contraseña son requeridos.")
    ENnombre3.delete(0,END)
    ENcontra3.delete(0,END)
    ENname1.delete(0,END)
    ENpass1.delete(0,END)
    ENcuenta2.delete(0,END)

# Metodo: ejecutar eliminar usuario
def deleteUser():
    exe.deleteAccount(nombre.get(),contra.get())
    ENnombre4.delete(0,END)
    ENcontra4.delete(0,END)

# -------------------------------------------------- Metodos de pestaña 2 -------------------------------------------------- #

# Metodo: ejecutar definir presupuesto
def definirPresupuesto():
    if dinero.get()=="":
        messagebox.showwarning("Advertencia","No has proporcionado un presupuesto!")
    else:
        p = float(dinero.get())
        exe.definirP(p)
        labelPresupuesto.config(text=f"Presupuesto ${p}")
    ENpresupuesto.delete(0,END)

# Metodo: ejecutar añadir transaccion
def exeAddTransaccion():
    index = panel2.index(panel2.select())
    if index==1:
        categoria = "Ingreso"
        tipo = tipoIngreso.get()
        if tipo=="Seleccionar":
            messagebox.showwarning("Advertencia!","Falta informacion!")
        else:
            nuevop = exe.addTransaccion(categoria,tipo,descripcion.get(),monto.get())
            labelPresupuesto.config(text=f"Presupuesto ${nuevop}")
        ENdescripcion1.delete(0,END)
        ENmonto1.delete(0,END)
    
    elif index==2:
        categoria = "Egreso"
        tipo = tipoEgreso.get()
        if tipo=="Seleccionar":
            messagebox.showwarning("Advertencia!","Falta informacion!")
        else:
            nuevop = exe.addTransaccion(categoria,tipo,descripcion.get(),monto.get())
            labelPresupuesto.config(text=f"Presupuesto ${nuevop}")
        ENdescripcion2.delete(0,END)
        ENmonto2.delete(0,END)
    tipoEgreso.set("Seleccionar")
    tipoIngreso.set("Seleccionar")

# Metodo: ejecutar mostrar transacciones
def exeShowTransacciones():
    tvTransacciones.delete(*tvTransacciones.get_children())
    registros = exe.showTransacciones()
    if registros:
        for i in registros:
            cadena = (i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            tvTransacciones.insert("",END,values=cadena)
    else:
        messagebox.showinfo("Datos inexistentes","No hay registros para mostrar")

# Metodo: ejecutar mostrar impuestos
def exeimpuestos():
    tvImpuestos.delete(*tvImpuestos.get_children())
    registros = exe.showTransacciones()
    if registros:
        for i in registros:
            cadena = (i[0],i[1],i[2],i[3])
            tvImpuestos.insert("",END,values=cadena)
    else:
        messagebox.showinfo("Datos inexistentes","No hay registros para mostrar")

def exeimptotales():
    totales = exe.impTotales()
    respuesta = messagebox.askyesno("Confirmacion","¿Desea saber la cantidad de impuestos totales?")
    if respuesta:
        messagebox.showinfo("Impuestos totales",f"La cantidad total es de ${totales}")
    else:
        messagebox.showwarning("Consulta de impuestos","No se mostraron los impuestos totales")

# Metodo: ejecutar cerrar sesion
def exeLogout():
    exe.logout()
    w2.withdraw()
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

btnRegistro = Button(p1_1,text="Registrar",font=("Century Gothic",12),command=exeSignUp)
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

btnIngreso = Button(p1_2,text="Ingresar",font=("Century Gothic",12),command=exeLogin)
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

label_fecha4 = Label(p1_4, font=("Century Gothic", 12))
label_fecha4.pack(side=BOTTOM,fill=BOTH,expand=True)
actualizar_fecha(label_fecha4)

# -------------------------------------------------- Widgets de pestaña 2 -------------------------------------------------- #

# Widgets ventana 2, pestaña presupuesto
titu0 = Label(presupuesto,text="Definir presupuesto",fg="green",font=("Century Gothic",16))
titu0.pack()
LBpresupuesto = Label(presupuesto,text="Presupuesto:",font=("Century Gothic",16))
LBpresupuesto.pack()
ENpresupuesto = Entry(presupuesto,textvariable=dinero)
ENpresupuesto.pack()

btnDefinir = Button(presupuesto,text="Definir Presupuesto",font=("Century Gothic",12),command=definirPresupuesto).pack()

labelPresupuesto = Label(presupuesto,text="Presupuesto $0",font=("Century Gothic",12))
labelPresupuesto.pack(side=BOTTOM,fill=BOTH,expand=True)

# Widgets ventana 2, pestaña 1
titu1 = Label(p2_1,text="Ingresos",fg="green",font=("Century Gothic",16))
titu1.pack()
LBtipo1 = Label(p2_1, text="Tipo:",font=("Century Gothic",12))
LBtipo1.pack()
tipoIngreso.set("Seleccionar")
OMtipo1 = OptionMenu(p2_1, tipoIngreso, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito")
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
titu2 = Label(p2_2,text="Egresos",fg="green",font=("Century Gothic",16))
titu2.pack()
LBtipo2 = Label(p2_2, text="Tipo:",font=("Century Gothic",12))
LBtipo2.pack()
tipoEgreso.set("Seleccionar")
OMtipo2 = OptionMenu(p2_2, tipoEgreso, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito")
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
titu3 = Label(p2_3,text="Impuestos",fg="green",font=("Century Gothic",16))
titu3.pack()

tvImpuestos = ttk.Treeview(p2_3,columns=('id','usuario_id','impuesto','fecha'),show="headings")
tvImpuestos.heading('#0', text="Index")
tvImpuestos.heading('id', text="Numero")
tvImpuestos.heading('usuario_id', text="Identificador de usuario")
tvImpuestos.heading('impuesto', text="Impuesto")
tvImpuestos.heading('fecha', text="Fecha")
tvImpuestos.pack(expand=True, fill=BOTH)

btnConsultarImpuestos = Button(p2_3,text="Consultar impuestos",font=("Century Gothic",12),command=exeimpuestos).pack()
btnImpuestosTotales = Button(p2_3,text="Impuestos Totales",font=("Century Gothic",12),command=exeimptotales).pack()

#Widgets Ventana 2 Pestaña 4
titu5 = Label(p2_4,text="Consultar Movimientos",fg="green",font=("Century Gothic",16)).pack()
btnConsultar = Button(p2_4,text="Consultar",font=("Century Gothic",16),command=exeShowTransacciones).pack()

tvTransacciones = ttk.Treeview(p2_4,columns=('id','categoria','tipo','descripcion','monto','usuario_id','fecha'),show="headings")
tvTransacciones.heading('#0',text="Index")
tvTransacciones.heading('id',text="Id")
tvTransacciones.heading('categoria',text="Categoria")
tvTransacciones.heading('tipo',text="Tipo")
tvTransacciones.heading('descripcion',text="Descripcion")
tvTransacciones.heading('monto',text="Monto")
tvTransacciones.heading('usuario_id',text="Identificador de Usuario")
tvTransacciones.heading('fecha',text="Fecha")
tvTransacciones.pack(expand=True, fill=BOTH)

# Widgets Ventana 2 Pestaña 5
titu6 = Label(p2_5,text="Cerrar Sesion",fg="green",font=("Century Gothic",16)).pack()
btnCloseSesion = Button(p2_5,text="Cerrar Sesion",font=("Century Gothic",12),command=exeLogout).pack()

# -------------------------------------------------- MAINLOOP -------------------------------------------------- #
w1.mainloop()