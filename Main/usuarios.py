from tkinter import messagebox
import sqlite3
import datetime

class usuarios:
    def __init__(self,nombre,contra,nocuenta,categoria,tipo,descripcion,monto):
        self.__nombre__ = nombre
        self.__contra__ = contra
        self.__nocuenta__ = nocuenta
        self.__categoria__ = categoria
        self.__tipo__ = tipo
        self.__descripcion__ = descripcion
        self.__monto__ = monto
        self.__presupuesto__ = 0
        self.__impuestos__ = 0
    
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
            nocuenta = self.__nocuenta__.get()
            if (nombre == "" or contra == "" or nocuenta==""):
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
    
    def updateInfo(self, name, password, ncuenta):
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
                        sql1 = "SELECT nombre, contrasena, cuenta FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
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
                        datos = (name,password,ncuenta,nombre)
                        consultaUpdateInfo = "UPDATE tbUsuarios SET nombre = ?, contrasena = ?, cuenta = ? WHERE nombre = ?"
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
                        return resultado[0]
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
    
    def definirP(self,presupuesto):
        try:
            self.__presupuesto__ = float(presupuesto)
            messagebox.showinfo("Presupuesto","Se ha definido un nuevo presupuesto de $"+str(self.__presupuesto__))
        except:
            print("No se pudo definir el presupuesto")
    
    def addTransaccion(self,categoria):
        try:
            conx = self.conexionDB()
            c3 = conx.cursor()
            tipo = self.__tipo__.get()
            descripcion = self.__descripcion__.get()
            monto = self.__monto__.get()
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
                        c3.execute(conseguirIDEsql,data)
                        resultado = c3.fetchone()
                        conx.commit()
                        return resultado[0]
                    ide = conseguirID()
                    datos = (categoria, tipo, descripcion, monto, ide, fecha)
                    consultaTransaccion = "INSERT INTO tbRegistros(categoria, tipo, descripcion, monto, usuario_id, fecha) VALUES (?, ?, ?, ?, ?, ?)"
                    c3.execute(consultaTransaccion,datos)
                    conx.commit()
                    conx.close()
                    if categoria=="Ingreso":
                        self.__presupuesto__ += float(monto)
                        messagebox.showinfo("Exito!","Registro completo!")
                        self.__impuestos__ += round(float(monto)*0.16,2)
                        return self.__presupuesto__
                    if categoria=="Egreso":
                        self.__presupuesto__ -= float(monto)
                        messagebox.showinfo("Exito!","Registro completo!")
                        return self.__presupuesto__
        except sqlite3.OperationalError:
            print("Error de consulta")
    
    def impuestos(self):
        try:
            conx = self.conexionDB()
            c10 = conx.cursor()
            nombre = self.__nombrelogin__
            contra = self.__contralogin__
            def conseguirID():
                data = (nombre,contra)
                conseguirIDEsql = "SELECT id FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                c10.execute(conseguirIDEsql,data)
                resultado = c10.fetchone()
                conx.commit()
                return resultado[0]
            ide = conseguirID()

            def obtenerUltimoImpuesto():
                data = (ide,)
                obtenerImpuestosSql = "SELECT impuesto FROM tbImpuestos WHERE usuario_id = ? ORDER BY fecha DESC LIMIT 1"
                c10.execute(obtenerImpuestosSql, data)
                resultado = c10.fetchone()
                conx.commit()
                return resultado[0] if resultado else 0.0

            ultimo_impuesto = obtenerUltimoImpuesto()
            impuesto = self.__impuestos__ + float(ultimo_impuesto)
            fecha = datetime.date.today().isoformat()
            data = (ide,impuesto,fecha)
            sqlImpuestos = "INSERT INTO tbImpuestos (usuario_id, impuesto, fecha) VALUES (?, ?, ?)"
            c10.execute(sqlImpuestos,data)
            conx.commit()
            conx.close()
            return impuesto
        except:
            print("Error de consulta")

    
    def showTransacciones(self):
        try:
            conx = self.conexionDB()
            c4 = conx.cursor()
            nombre = self.__nombrelogin__
            contra = self.__contralogin__
            def conseguirID():
                data = (nombre,contra)
                conseguirIDEsql = "SELECT id FROM tbUsuarios WHERE nombre = ? and contrasena = ?"
                c4.execute(conseguirIDEsql,data)
                resultado = c4.fetchone()
                conx.commit()
                return resultado[0]
            ide = conseguirID()
            consultaMostrarTransacciones = "SELECT * FROM tbRegistros WHERE usuario_id = ?"
            c4.execute(consultaMostrarTransacciones,(ide,))
            registros = c4.fetchall()
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