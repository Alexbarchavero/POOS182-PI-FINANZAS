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

@app.route("/guardar", methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vnombre=request.form['nombre']
        Vcontrasena=request.form['contrasena']
        Vcuenta=request.form['cuenta']
        
        cs = mysql.connection.cursor()
        cs.execute('insert into tbUsuarios (nombre, contrasena, cuenta) values (%s, %s, %s)', (Vnombre,Vcontrasena,Vcuenta))
        mysql.connection.commit()

    flash('Usuario registrado correctamente')
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)