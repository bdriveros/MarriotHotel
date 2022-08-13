from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Producto(FlaskForm):
    codigo = StringField('id', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    precio = StringField('Precio', validators=[DataRequired()])
    cantidad = StringField('Cantidad', validators=[DataRequired()])
    enviar = SubmitField('Agregar Producto')

class Usuarios(FlaskForm):
    Id = StringField('Id', validators=[DataRequired()])
    Nombres = StringField('Nombres', validators=[DataRequired()])
    Apellidos = StringField('Apellidos', validators=[DataRequired()])
    Celular = StringField('Celular', validators=[DataRequired()])
    Correo = StringField('Correo', validators=[DataRequired()])
    Username = StringField('Username', validators=[DataRequired()])
    Password = StringField('Password', validators=[DataRequired()])
    enviar = SubmitField('Registrarse')