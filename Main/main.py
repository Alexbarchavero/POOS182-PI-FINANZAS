from tkinter import ttk, Tk, Toplevel, Frame, StringVar, BOTH, Label, Entry, Button, OptionMenu, END
from tkinter import *
from usuarios import *

# Creamos la ventana 1 centrada
w1 = Tk()
w1.title("Inicio")
ancho1 = w1.winfo_screenwidth()
alto1 = w1.winfo_screenheight()
w1_ancho = 480
w1_alto = 320
x = int((ancho1-w1_ancho)/2)
y = int((alto1-w1_alto)/2)
w1.geometry("{}x{}+{}+{}".format(w1_ancho,w1_alto,x,y))
# Creamos el Notebook para la ventana 1
panel1 = ttk.Notebook(w1)
panel1.pack(fill = BOTH, expand = True)
p1_1 = Frame(panel1)
p1_2 = Frame(panel1)
# Nombramos las pestañas en el panel
panel1.add(p1_1, text = "Registrarse")
panel1.add(p1_2, text = "Iniciar sesion")

# Creamos la ventana 2 centrada
w2 = Toplevel(w1)
w2.title("Finanzas")
ancho2 = w2.winfo_screenwidth()
alto2 = w2.winfo_screenheight()
w2_ancho = 480
w2_alto = 320
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
nombre = StringVar()
contra = StringVar()
categoria = StringVar()
tipo = StringVar()
descripcion = StringVar()
monto = StringVar()

# Instancia
exe = usuarios(nombre,contra,categoria,tipo,descripcion,monto)

# Metodo: ejecutar registrar usuario
def exeSignUp():
    exe.signup()
    ENnombre1.delete(0, END)
    ENcontra1.delete(0, END)

# Metodo: ejecutar iniciar sesion
def exeLogin():
    exe.login()
    ENnombre2.delete(0, END)
    ENcontra2.delete(0, END)
    w1.withdraw()
    w2.deiconify()

# Metodo: ejecutar añadir transaccion
def exeAddTransaccion():
    index = panel2.index(panel2.select())
    if index==0:
        categoria = "Ingreso"
    elif index==1:
        categoria = "Gasto"
    elif index==2:
        categoria = "Compra"
    elif index==3:
        categoria = "Pago"
    exe.addTransaccion(categoria)

# Metodo: ejecutar cerrar sesion
def exeLogout():
    exe.logout()
    w2.destroy()
    w1.deiconify()

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

# Etiquetas, entrys y boton de ventana 1, pestaña 1
titulo1 = Label(p1_1,text="Finanzas",font=("Century Gothic",16))
titulo1.pack()

LBnombre1 = Label(p1_1,text="Ingrese su Nombre: ",font=("Century Gothic",12))
LBnombre1.pack()
ENnombre1 = Entry(p1_1,textvariable=nombre)
ENnombre1.pack()

LBcontra1 = Label(p1_1,text="Ingrese una Contraseña: ",font=("Century Gothic",12))
LBcontra1.pack()
ENcontra1 = Entry(p1_1,textvariable=contra)
ENcontra1.pack()

btnRegistro = Button(p1_1,text="Registrar",font=("Century Gothic",12),bg="light blue",command=exeSignUp)
btnRegistro.pack()

# Etiquetas, entrys y boton de ventana 1, pestaña 2
titulo2 = Label(p1_2,text="Finanzas",font=("Century Gothic",16))
titulo2.pack()

LBnombre2 = Label(p1_2,text="Ingrese su Nombre: ",font=("Century Gothic",12))
LBnombre2.pack()
ENnombre2 = Entry(p1_2,textvariable=nombre)
ENnombre2.pack()

LBcontra2 = Label(p1_2,text="Ingrese su Contraseña: ",font=("Century Gothic",12))
LBcontra2.pack()
ENcontra2 = Entry(p1_2,textvariable=contra)
ENcontra2.pack()

btnIngreso = Button(p1_2,text="Ingresar",font=("Century Gothic",12),bg="light green",command=exeLogin)
btnIngreso.pack()

# Etiquetas, entrys y botones de ventana 2, pestaña 1
titu1 = Label(p2_1,text="Ingresos",fg="blue",font=("Century Gothic",16)).pack()
LBtipo1 = Label(p2_1, text="Tipo:",font=("Century Gothic",12)).pack()
tipo.set("Seleccionar")
OMtipo1 = OptionMenu(p2_1, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito").pack()
LBdescripcion1 = Label(p2_1, text="Descripción:",font=("Century Gothic",12)).pack()
ENdescripcion1 = Entry(p2_1,textvariable=descripcion).pack()
LBmonto1 = Label(p2_1, text="Monto:",font=("Century Gothic",12)).pack()
ENmonto1 = Entry(p2_1,textvariable=monto).pack()

btnAddRegistro1 = Button(p2_1,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

# Etiquetas, entrys y botones de ventana 2, pestaña 2
titu2 = Label(p2_2,text="Gastos",fg="blue",font=("Century Gothic",16)).pack()
LBtipo2 = Label(p2_2, text="Tipo:",font=("Century Gothic",12)).pack()
tipo.set("Seleccionar")
OMtipo2 = OptionMenu(p2_2, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito").pack()
LBdescripcion2 = Label(p2_2, text="Descripción:",font=("Century Gothic",12)).pack()
ENdescripcion2 = Entry(p2_2,textvariable=descripcion).pack()
LBmonto2 = Label(p2_2, text="Monto:",font=("Century Gothic",12)).pack()
ENmonto2 = Entry(p2_2,textvariable=monto).pack()

btnAddRegistro2 = Button(p2_2,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

# Etiquetas, entrys y botones de ventana 2, pestaña 3
titu3 = Label(p2_3,text="Compras",fg="blue",font=("Century Gothic",16)).pack()
LBtipo3 = Label(p2_3, text="Tipo:",font=("Century Gothic",12)).pack()
tipo.set("Seleccionar")
OMtipo3 = OptionMenu(p2_3, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito").pack()
LBdescripcion3 = Label(p2_3, text="Descripción:",font=("Century Gothic",12)).pack()
ENdescripcion3 = Entry(p2_3,textvariable=descripcion).pack()
LBmonto3 = Label(p2_3, text="Monto:",font=("Century Gothic",12)).pack()
ENmonto3 = Entry(p2_3,textvariable=monto).pack()

btnAddRegistro3 = Button(p2_3,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

# Etiquetas, entrys y botones de ventana 2, pestaña 4
titu4 = Label(p2_4,text="Pagos",fg="blue",font=("Century Gothic",16)).pack()
LBtipo4 = Label(p2_4, text="Tipo:",font=("Century Gothic",12)).pack()
tipo.set("Seleccionar")
OMtipo4 = OptionMenu(p2_4, tipo, "Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito").pack()
LBdescripcion4 = Label(p2_4, text="Descripción:").pack()
ENdescripcion4 = Entry(p2_4,textvariable=descripcion).pack()
LBmonto4 = Label(p2_4, text="Monto:").pack()
ENmonto4 = Entry(p2_4,textvariable=monto).pack()

btnAddRegistro4 = Button(p2_4,text="Añadir transaccion",font=("Century Gothic",12),command=exeAddTransaccion).pack()

#Widgets Ventana 2 Pestaña 5
titu5 = Label(p2_5,text="Consultar Registros",fg="blue",font=("Century Gothic",16)).pack()
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
titu6 = Label(p2_6,text="Cerrar Sesion",fg="blue",font=("Century Gothic",16)).pack()
btnCloseSesion = Button(p2_6,text="Cerrar Sesion",font=("Century Gothic",12),command=exeLogout).pack()

# Mainloop
w1.mainloop()