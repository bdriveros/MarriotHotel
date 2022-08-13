from flask import request, Flask,flash, render_template, jsonify, url_for,session,make_response,g
import database as bd
from forms import Producto
from forms import Usuarios
from settings.config import configuracion


app = Flask(__name__)
app.config.from_object(configuracion)

@app.route('/main')
def main():
    return render_template('main.html',titulo="Marriot - Wuxi Moaye City ")

@app.route('/')
def inicio():
    return render_template('initial.html',titulo="Marriot - Wuxi Moaye City ")

@app.route('/details')
def detalleHabitacion():
    return render_template('details.html',titulo="Habitación x")

@app.route('/login')
def login():
    if request.method =='GET':
        form = Usuarios()
        return render_template('login.html',form=form,titulo="Registrate")
    elif request.method == 'POST':
        Username = request.form["Username"]
        Password = request.form["Passsword"]
        return render_template('login.html', titulo="Bienvenido")

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if request.method =='GET':
        form = Usuarios()
        return render_template('signup.html',form=form,titulo="Registrate")
    elif request.method == 'POST':
        Id = request.form["Id"]
        Nombres = request.form["Nombres"]
        Apellidos = request.form["Apellidos"]
        Celular = request.form["Celular"]
        Correo = request.form["Correo"]
        Username = request.form["Username"]
        Password = request.form["Password"]
        bd.sql_signup(Id,Nombres,Apellidos,Correo,Celular,Username,Password)
        flash(f'Usuario {Nombres} registrado con exito!')
        return render_template('initial.html',titulo="Registro de nuevo producto")

app.run(debug=True)