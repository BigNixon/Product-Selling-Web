import pymysql
from flask.helpers import url_for
from flask import Flask, render_template,request,redirect,flash
from venta import *

#==========================Conection with database =========================
connection=pymysql.connect(
            host="127.0.0.1", # si es remota coloca dominio // local tu IP
            user='root',
            password="pencilred28",
            db='productosdb',)

cursor = connection.cursor()

#========================= CLASSES AND METHODS ===========================

def obtener_productos():
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM productos")
            productx = cursor.fetchall()
            return productx
        except Exception as e:
            raise



#====================== START OF THE APPLICATION =======================
app = Flask(__name__)

@app.route('/index.html',methods=["get","post"])
def index():
    return render_template('index.html')

@app.route('/carrito.html',methods=["get","post"])
def carrito():
    return render_template('carrito.html')

@app.route('/admin.html')
def administracion():
    return render_template('admin.html')

@app.route('/guardar.html',methods=["POST"])
def guardarproducto():
    idproducto=request.form["id_Producto"]
    nombreproducto=request.form["Nombre_Producto"]
    precioproducto=request.form["precio_Producto"]
    cantidadproducto=request.form["cant_Producto"]
    proveedorproducto=request.form["proveedor_Producto"]
    producto1=producto(idproducto,nombreproducto,precioproducto,cantidadproducto,proveedorproducto)
    cursor.execute(producto1.asignacion(),(idproducto,nombreproducto,precioproducto,cantidadproducto,proveedorproducto))
    connection.commit()
    return redirect("/admin.html")

@app.route('/productos.html')
def productos():
    producto = obtener_productos()
    return render_template("productos.html", producto=producto)


@app.route('/recibir_pedido', methods=["post"])
def recibir_pedidos():
    pedido = pedidos("bugsbunny",10,123456789)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
