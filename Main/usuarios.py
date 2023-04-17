from tkinter import messagebox
import sqlite3
import datetime

class usuarios:
    def __init__(self):
        self.__impuestos__ = 0
        self.__presupuesto__ = 0
    
    def conexionDB(self):
        try:
            conexion = sqlite3.connect("C:/Users/Alejandro/Documents/GitHub/POOS182-PI-FINANZAS/Database/ControlDeFinanzas.db")
            print("Conexion correcta")
            return conexion
        except sqlite3.OperationalError:
            print("Error de conexion")
    
    # -------------------------------------------------- Funciones de la ventana 1 -------------------------------------------------- #
    
    def signup(self,nombre,contra,nocuenta):
        try:
            conx = self.conexionDB()
            if (nombre == "" or contra== "" or nocuenta==""):
                messagebox.showwarning("Advertencia","Campos incompletos")
                conx.close()
            else:
                c1 = conx.cursor()
                datos = (nombre,contra,nocuenta)
                consultaSignup = "INSERT INTO tbUsuarios(nombre, contrasena, cuenta) VALUES(?,?,?)"
                c1.execute(consultaSignup,datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito","Registro exitoso")
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def login(self,nombre,contra):
        try:
            conx = self.conexionDB()
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
                    self.__nombrelogin__ = nombre
                    self.__contralogin__ = contra
                    r = True
                else:
                    messagebox.showerror("Error","Usuario o contraseña incorrectos")
                    r = False
                conx.close()
                return r
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def updateInfo(self, nombre, contra, name, password, ncuenta):
        try:
            conx = self.conexionDB()
            c3 = conx.cursor()
            if (nombre=="" or contra==""):
                messagebox.showwarning("Advertencia","Faltan datos por ingresar")
                conx.close()
            else:
                def validar():
                    try:
                        datos1 = (nombre,contra)
                        sql1 = "SELECT nombre, contrasena, cuenta FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                        c3.execute(sql1,datos1)
                        resultado = c3.fetchone()
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
                        datos = (name,password,ncuenta,nombre)
                        consultaUpdateInfo = "UPDATE tbUsuarios SET nombre = ?, contrasena = ?, cuenta = ? WHERE nombre = ?"
                        c3.execute(consultaUpdateInfo,datos)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Exito","Datos actualizados")
                    else:
                        messagebox.showinfo("Informacion","Datos no actualizados")
                        conx.close()
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def deleteAccount(self, nombre, contra):
        try:
            conx = self.conexionDB()
            c4 = conx.cursor()
            if (nombre=="" or contra==""):
                messagebox.showwarning("Advertencia","Faltan datos")
            else:
                def validar():
                    try:
                        datos1 = (nombre,contra)
                        sql1 = "SELECT nombre, contrasena FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                        c4.execute(sql1,datos1)
                        resultado = c4.fetchone()
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
                        c4.execute(conseguirIDEsql,data)
                        resultado = c4.fetchone()
                        conx.commit()
                        return resultado[0]
                    ide = conseguirID()
                    answer = messagebox.askyesno("Confirmacion","¿Desea eliminar su cuenta?")
                    if answer:
                        consultaEliminarCuenta = "DELETE FROM tbUsuarios WHERE id = ?"
                        c4.execute(consultaEliminarCuenta,ide)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Exito","La cuenta ha sido eliminada correctamente")
                    else:
                        messagebox.showwarning("Advertencia","La cuenta no ha sido eliminada")
                        conx.close()
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    # -------------------------------------------------- Funciones de la ventana 2 -------------------------------------------------- #
    
    def definirP(self,presupuesto):
        try:
            self.__presupuesto__ = float(presupuesto)
            messagebox.showinfo("Presupuesto","Se ha definido un nuevo presupuesto de $"+str(self.__presupuesto__))
        except:
            print("No se pudo definir el presupuesto")
    
    def addTransaccion(self, categoria, tipo, descripcion, monto):
        try:
            conx = self.conexionDB()
            c5 = conx.cursor()
            nombre = self.__nombrelogin__
            contra = self.__contralogin__
            fecha = datetime.date.today().isoformat()
            
            if (descripcion=="" or monto==""):
                messagebox.showwarning("Advertencia!","Falta informacion!")
                conx.close()
            else:
                if (categoria=="Egreso" and float(monto)>self.__presupuesto__):
                    messagebox.showwarning("Advertencia!","El monto excede el presupuesto dado!")
                    self.__presupuesto__ = self.__presupuesto__
                    conx.close()
                    return self.__presupuesto__
                else:
                    def conseguirID():
                        data = (nombre,contra)
                        conseguirIDEsql = "SELECT id FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                        c5.execute(conseguirIDEsql,data)
                        resultado = c5.fetchone()
                        conx.commit()
                        return resultado[0]
                    ide = conseguirID()
                    datos = (categoria, tipo, descripcion, monto, ide, fecha)
                    consultaTransaccion = "INSERT INTO tbRegistros(categoria, tipo, descripcion, monto, usuario_id, fecha) VALUES (?, ?, ?, ?, ?, ?)"
                    c5.execute(consultaTransaccion,datos)
                    if categoria=="Ingreso":
                        self.__presupuesto__ += float(monto)
                        messagebox.showinfo("Exito!","Registro completo!")
                        c5 = conx.cursor()
                        imp = float(monto)*0.16
                        data = (ide,imp,fecha)
                        slqsentence = "INSERT INTO tbImpuestos (usuario_id,impuesto,fecha) VALUES (?, ?, ?)"
                        c5.execute(slqsentence,data)
                        conx.commit()
                        conx.close()
                        return self.__presupuesto__
                    else:
                        self.__presupuesto__ -= float(monto)
                        messagebox.showinfo("Exito!","Registro completo!")
                        conx.close()
                        return self.__presupuesto__
        except sqlite3.OperationalError:
            print("Error de consulta")
     
    def impuestos(self):
        try:
            conx = self.conexionDB()
            c6 = conx.cursor()
            nombre = self.__nombrelogin__
            contra = self.__contralogin__
            def conseguirID():
                data = (nombre,contra)
                conseguirIDEsql = "SELECT id FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                c6.execute(conseguirIDEsql,data)
                resultado = c6.fetchone()
                conx.commit()
                return resultado[0]
            ide = conseguirID()
            sql = "SELECT * FROM tbImpuestos WHERE usuario_id = ?"
            c6.execute(sql,(ide,))
            registros = c6.fetchall()
            conx.commit()
            conx.close()
            return registros
        except sqlite3.OperationalError:
            print("Error de consulta: ")
    
    def impTotales(self):
        try:
            conx = self.conexionDB()
            c7 = conx.cursor()
            nombre = self.__nombrelogin__
            contra = self.__contralogin__
            def conseguirID():
                data = (nombre,contra)
                conseguirIDEsql = "SELECT id FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                c7.execute(conseguirIDEsql,data)
                resultado = c7.fetchone()
                conx.commit()
                return resultado[0]
            
            ide = conseguirID()
            sql = "SELECT SUM(impuesto) FROM tbImpuestos WHERE usuario_id = ?"
            c7.execute(sql, (ide,))
            resultado = c7.fetchone()[0]
            return resultado
        except sqlite3.OperationalError:
            print("Error de consulta")

    
    def showTransacciones(self):
        try:
            conx = self.conexionDB()
            c8 = conx.cursor()
            nombre = self.__nombrelogin__
            contra = self.__contralogin__
            def conseguirID():
                data = (nombre,contra)
                conseguirIDEsql = "SELECT id FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                c8.execute(conseguirIDEsql,data)
                resultado = c8.fetchone()
                conx.commit()
                return resultado[0]
            ide = conseguirID()
            consultaMostrarTransacciones = "SELECT * FROM tbRegistros WHERE usuario_id = ?"
            c8.execute(consultaMostrarTransacciones,(ide,))
            registros = c8.fetchall()
            conx.commit()
            conx.close()
            return registros
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def logout(self):
        self.__nombre__ = None
        self.__contra__ = None
        self.__presupuesto__ = 0
        self.__impuestos__ = 0
        messagebox.showinfo("Cerrar sesion","Cierre de sesion exitoso")