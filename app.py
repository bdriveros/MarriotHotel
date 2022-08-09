from flask import request, Flask,flash, render_template, jsonify, url_for
import database as bd
from forms import Producto
from settings.config import configuracion


app = Flask(__name__)
app.config.from_object(configuracion)

@app.route('/')
def api():
    return render_template('index.html',titulo="Ejemplo SQLite")

@app.route('/productos')
def getProductos():
    lista_productos = bd.sql_select_productos()
    flash("Lista de productos")
    return render_template('productos.html',l_productos=lista_productos,titulo="Lista de productos")

@app.route('/nuevo',methods=['GET', 'POST'])
def nuevo():
    if request.method =='GET':
        form = Producto()
        return render_template('nuevo.html',form=form,titulo="Registro de nuevo producto")
    elif request.method == 'POST':
        codigo = request.form["codigo"]
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        cantidad = request.form["cantidad"]
        bd.sql_insert_producto(codigo, nombre, precio, cantidad)
        flash(f'producto {nombre} registrado con exito!')
        return render_template('base.html',titulo="Registro de nuevo producto")

@app.route('/edit',methods=['GET'])
def editarProducto():
    codigo = request.args.get("codigo")
    cantidad = request.args.get("cantidad")
    bd.sql_edit_producto(codigo, cantidad)
    flash(f'producto {codigo} actualizado con exito')
    return render_template('base.html',titulo="Producto actualizado")


@app.route('/delete',methods=['GET'])
def eliminarProducto():
    codigo = request.args.get("codigo")
    bd.sql_delete_producto(codigo)
    flash(f'producto {codigo} eliminado con exito')
    return render_template('base.html',titulo="Producto eliminado")

app.run(debug=True)