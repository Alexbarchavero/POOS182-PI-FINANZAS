from tkinter import messagebox
import sqlite3

class usuarios:
    def __init__(self,nombre,contra,categoria,tipo,descripcion,monto):
        self.__nombre__ = nombre
        self.__contra__ = contra
        self.__categoria__ = categoria
        self.__tipo__ = tipo
        self.__descripcion__ = descripcion
        self.__monto__ = monto
    
    def conexionDB(self):
        try:
            conexion = sqlite3.connect("C:/Users/Alejandro/Documents/GitHub/POOS182-PI-FINANZAS/Database/ControlDeFinanzas.db")
            print("Conexion correcta")
            return conexion
        except sqlite3.OperationalError:
            print("Error de conexion")
    
    def obtenerId(self,nombre):
        try:
            conx = self.conexionDB()
            c0 = conx.cursor()
            datos = (nombre,)
            consultaObtenerId = "SELECT id FROM tbUsuarios where nombre = ?"
            c0.execute(consultaObtenerId,datos)
            resultado = c0.fetchone()
            if resultado:
                ide = resultado[0]
            else:
                print("No existe el Usuario")
            return ide
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def signup(self):
        try:
            conx = self.conexionDB()
            nombre = self.__nombre__.get()
            contra = self.__contra__.get()
            if (nombre == "" or contra == ""):
                messagebox.showwarning("Advertencia","Campos incompletos")
                conx.close()
            else:
                c1 = conx.cursor()
                datos = (nombre,contra)
                consultaSignup = "INSERT INTO tbUsuarios(nombre, contrasena) VALUES(?,?)"
                c1.execute(consultaSignup,datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito","Registro exitoso")
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def login(self):
        try:
            conx = self.conexionDB()
            nombre = self.__nombre__.get()
            contra = self.__contra__.get()
            if (nombre == "" or contra == ""):
                messagebox.showwarning("Advertencia","Campos incompletos")
                conx.close()
            else:
                c2 = conx.cursor()
                datos = (nombre,contra)
                consultaLogin = "SELECT * FROM tbUsuarios WHERE nombre = ? AND contrasena = ?"
                c2.execute(consultaLogin,datos)
                resultado = c2.fetchone()
                if resultado:
                    self.__username__ = nombre
                    messagebox.showinfo("Exito","Inicio de sesión exitoso")
                    self.r = True
                else:
                    messagebox.showerror("Error","Usuario o contraseña incorrectos")
                    self.r = False
                conx.close()
                return self.r
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def logout(self):
        self.__username__ = None
        print("Cierre de sesion exitoso")
    
    def addTransaccion(self,categoria):
        try:
            conx = self.conexionDB()
            tipo = self.__tipo__.get()
            descripcion = self.__descripcion__.get()
            monto = self.__monto__.get()
            if (descripcion=="" or monto==""):
                messagebox.showwarning("Advertencia!","Falta informacion!")
                conx.close()
            else:
                usuario_id = self.obtenerId(self.__username__)
                c3 = conx.cursor()
                datos = (categoria, tipo, descripcion, monto, usuario_id)
                consultaTransaccion = "INSERT INTO tbRegistros(categoria, tipo, descripcion, monto, usuario_id) VALUES (?, ?, ?, ?, ?)"
                c3.execute(consultaTransaccion,datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito!","Registro completo!")
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def showTransacciones(self):
        try:
            conx = self.conexionDB()
            usuario_id = self.obtenerId(self.__username__)
            c4 = conx.cursor()
            datos = (usuario_id,)
            consultaMostrarTransacciones = "SELECT * FROM tbRegistros where usuario_id = ?"
            c4.execute(consultaMostrarTransacciones,datos)
            registros = c4.fetchall()
            conx.commit()
            conx.close()
            return registros
        except sqlite3.OperationalError:
            print("Error de consulta")
    def showUserinfo(self):
        try:
            nombre = self.__nombre__.get()
        except:
            print("No jalo")
#Según los 2 archivos que te acabo de proporcionar, 