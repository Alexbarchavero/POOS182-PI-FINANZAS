from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] ='finanzas'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route("/")
def inicio():
    return render_template('inicio.html')

@app.route("/finanzas", methods = ['POST'])
def finanzas():
    if request.method == 'POST':
        ISnombre = request.form['nombre-login']
        IScontrasena = request.form['contrasena-login']
        
        cis = mysql.connection.cursor()
        cis.execute('select * from tbusuarios where nombre = %s and contrasena = %s',(ISnombre, IScontrasena))
        consulta = cis.fetchone()
        mysql.connection.commit()
        if consulta is not None:
            flash("Inicio de sesion correcto!")
            return render_template('finanzas.html')
        else:
            flash("Inicio de sesion incorrecto!")
            return render_template('inicio.html')

@app.route("/registrar", methods=['POST'])
def registrar():
    if request.method == 'POST':
        Vnombre=request.form['nombre']
        Vcontrasena=request.form['contrasena']
        Vcuenta=request.form['cuenta']
        
        cr = mysql.connection.cursor()
        cr.execute('insert into tbusuarios (nombre, contrasena, cuenta) values (%s, %s, %s)', (Vnombre,Vcontrasena,Vcuenta))
        mysql.connection.commit()
    flash('Usuario registrado correctamente')
    return redirect(url_for('inicio'))



@app.route("/actualizar", methods=['POST'])
def actualizar():
    if request.method == 'POST':
        Anombrea = request.form['nombre-actual']
        Acontrasenaa = request.form['contrasena-actual']
        Anombren = request.form['nuevo-nombre']
        Acontrasenan = request.form['nueva-contrasena']
        Acuentan = request.form['nueva-cuenta']
        
        ca = mysql.connection.cursor()
        ca.execute('update tbusuarios set nombre = %s, contrasena = %s, cuenta = %s where nombre = %s and contrasena = %s', (Anombren, Acontrasenan, Acuentan, Anombrea, Acontrasenaa))
        mysql.connection.commit()
    flash('Usuario actualizado correctamente')
    return redirect(url_for('inicio'))

@app.route("/eliminar", methods=['POST'])
def eliminar():
    if request.method == 'POST':
        Enombre = request.form['nombre-eliminar']
        Econtrasena = request.form['contrasena-eliminar']
        
        ce = mysql.connection.cursor()
        ce.execute('delete from tbusuarios where nombre = %s and contrasena = %s',(Enombre, Econtrasena))
        mysql.connection.commit()
    flash('Usuario eliminado correctamente')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)