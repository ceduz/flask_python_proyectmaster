from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

aplicacion = Flask(__name__)
#Coneción a la base de datos en que servidor y usuario contraseña y la base de datos.
aplicacion.config['MYSQL_HOST'] = 'localhost' 
aplicacion.config['MYSQL_USER'] = 'root'
aplicacion.config['MYSQL_PASSWORD'] = 'admin'
aplicacion.config['MYSQL_DB'] = 'flasktutorias'
mysql = MySQL(aplicacion)

# configuraciones mysecretkey para flash
aplicacion.secret_key = 'mysecretkey'

@aplicacion.route('/')
def Index():
    #creo variable cursor y envio la coneccion a la base de datos
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tutoria')
    datos = cur.fetchall()
    return render_template('index.html', tutoria = datos)

@aplicacion.route('/add_tutoria', methods=['POST'])
def add_tutorias():
    if request.method == 'POST':
        id_profesor = request.form['id_profesor']
        nombre_profesor = request.form['nombre_profesor']
        apellidos_profesor = request.form['apellidos_profesor']
        tema_tutoria = request.form['tema_tutoria']
        dia_tutoria = request.form['lista_dia']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        lugar_tutoria = request.form['lugar_tutoria']
        email_profesor = request.form['email_profesor']
        
        #creo variable cursor y envio la coneccion a la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tutoria (id_profesor, nombre_profesor, apellidos_profesor, tema_tutoria, dia_tutoria, hora_inicio, hora_fin, lugar_tutoria, email_profesor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (id_profesor, nombre_profesor, apellidos_profesor, tema_tutoria, dia_tutoria, hora_inicio, hora_fin, lugar_tutoria, email_profesor))
        mysql.connection.commit()

        flash('Tutoria agregada Exitosamente')

        return redirect(url_for('Index'))
    

@aplicacion.route('/editar/<string:id>')
def get_tutoria(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tutoria WHERE id_tutoria = {0}'.format(id))
    datos = cur.fetchall()
    return render_template('edit-tutoria.html', tuto = datos[0])

@aplicacion.route('/actualizacion/<id>', methods=['POST'])
def actualizacion_tutoria(id):
    if request.method == 'POST':
        id_profesor = request.form['id_profesor']
        nombre_profesor = request.form['nombre_profesor']
        apellidos_profesor = request.form['apellidos_profesor']
        tema_tutoria = request.form['tema_tutoria']
        dia_tutoria = request.form['lista_dia']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']
        lugar_tutoria = request.form['lugar_tutoria']
        email_profesor = request.form['email_profesor']
        
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE tutoria
                SET id_profesor = %s,
                nombre_profesor = %s,
                apellidos_profesor = %s,
                tema_tutoria = %s,
                dia_tutoria = %s,
                hora_inicio = %s,
                hora_fin = %s,
                lugar_tutoria = %s,
                email_profesor = %s
            WHERE id_tutoria = %s
            """, (id_profesor, nombre_profesor, apellidos_profesor, tema_tutoria, dia_tutoria, hora_inicio, hora_fin, lugar_tutoria, email_profesor, id))
        mysql.connection.commit()
        flash('Tutoria actualizada exitosamente.')
        return redirect(url_for('Index'))

@aplicacion.route('/borrar/<string:id>')#espesificando el tipo de dato
def borrar_tutoria(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tutoria WHERE id_tutoria = {0}'.format(id)) #en la posición 0 ira el id formateado en string
    mysql.connection.commit()
    flash('Tutoria eliminada Exitosamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    aplicacion.run(port = 3000, debug = True)