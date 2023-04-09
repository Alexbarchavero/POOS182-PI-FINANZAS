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
    
    # -------------------------------------------------- Funciones de la ventana 1 -------------------------------------------------- #
    
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
                    messagebox.showinfo("Exito","Inicio de sesión exitoso")
                    r = True
                else:
                    messagebox.showerror("Error","Usuario o contraseña incorrectos")
                    r = False
                conx.close()
                return r
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def updateInfo(self, name, password):
        try:
            conx = self.conexionDB()
            nombre = self.__nombre__.get()
            contra = self.__contra__.get()
            c6 = conx.cursor()
            if (nombre=="" or contra==""):
                messagebox.showwarning("Advertencia","Faltan datos por ingresar")
                conx.close()
            else:
                def validar():
                    try:
                        datos1 = (nombre,contra)
                        sql1 = "SELECT nombre, contrasena FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                        c6.execute(sql1,datos1)
                        resultado = c6.fetchone()
                        if resultado:
                            conx.commit()
                            return resultado
                    except sqlite3.OperationalError:
                        print("Error de consulta")
                if validar() is None:
                    messagebox.showerror(
                        "Error",
                        "El nombre y/o la contraseña proporcionados no son correctos o no coinciden en la base de datos"
                    )
                    conx.close()
                else:
                    resultado = messagebox.askyesno("Confirmacion","¿Esta seguro de actualizar sus datos?")
                    if resultado:
                        datos = (name,password,nombre)
                        consultaUpdateInfo = "UPDATE tbUsuarios SET nombre = ?, contrasena = ? WHERE nombre = ?"
                        c6.execute(consultaUpdateInfo,datos)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Exito","Datos actualizados")
                    else:
                        messagebox.showinfo("Informacion","Datos no actualizados")
                        conx.close()
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def deleteAccount(self):
        try:
            conx = self.conexionDB()
            nombre = self.__nombre__.get()
            contra = self.__contra__.get()
            c7 = conx.cursor()
            if (nombre=="" or contra==""):
                messagebox.showwarning("Advertencia","Faltan datos")
            else:
                def validar():
                    try:
                        datos1 = (nombre,contra)
                        sql1 = "SELECT nombre, contrasena FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                        c7.execute(sql1,datos1)
                        resultado = c7.fetchone()
                        if resultado:
                            conx.commit()
                            return resultado
                    except sqlite3.OperationalError:
                        print("Error de consulta")
                
                if validar() is None:
                    messagebox.showerror("Error","Los datos son incorrectos o no coinciden con algun usuario registrado")
                    conx.close()
                else:
                    def conseguirID():
                        data = (nombre,contra)
                        conseguirIDEsql = "SELECT id FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                        c7.execute(conseguirIDEsql,data)
                        resultado = c7.fetchone()
                        conx.commit()
                        return resultado
                    ide = conseguirID()
                    answer = messagebox.askyesno("Confirmacion","¿Desea eliminar su cuenta?")
                    if answer:
                        consultaEliminarCuenta = "DELETE FROM tbUsuarios WHERE id = ?"
                        c7.execute(consultaEliminarCuenta,ide)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Exito","La cuenta ha sido eliminada correctamente")
                    else:
                        messagebox.showwarning("Advertencia","La cuenta no ha sido eliminada")
                        conx.close()
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    # -------------------------------------------------- Funciones de la ventana 2 -------------------------------------------------- #
    
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
    
    def logout(self):
        self.__nombre__ = None
        self.__contra__ = None
        messagebox.showinfo("Cerrar sesion","Cierre de sesion exitoso")