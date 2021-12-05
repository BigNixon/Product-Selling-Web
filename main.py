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

def obtener_carrito():
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM carrito")
            carrito = cursor.fetchall()
            return carrito
        except Exception as e:
            raise

def obtener_ventas():
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM ventas")
            venta = cursor.fetchall()
            return venta
        except Exception as e:
            raise
            
def limpiar_carrito():
    global vecesp1,vecesp2,vecesp3,vecesp4,vecesp5,vecesp6,vecesp7,vecesp8,aux1,aux2,aux3,aux4,aux5,aux6,aux7,aux8
    vecesp1,vecesp2,vecesp3,vecesp4,vecesp5,vecesp6,vecesp7,vecesp8=1,1,1,1,1,1,1,1
    aux1,aux2,aux3,aux4,aux5,aux6,aux7,aux8=0,0,0,0,0,0,0,0
    with connection.cursor() as cursor:
        try:
            cursor.execute("DELETE FROM carrito")
            carrito = cursor.fetchall()
            return carrito
        except Exception as e:
            raise

#====================== START OF THE APPLICATION =======================
app = Flask(__name__)

@app.route('/index.html',methods=["get","post"])
def index():
    return render_template('index.html')

@app.route('/carrito.html',methods=["get","post"])
def carrito():
    carrito = obtener_carrito()
    return render_template('carrito.html', carrito=carrito)

@app.route('/login.html', methods=["post","get"])
def login():
    return render_template("login.html")

@app.route('/admin.html')
def administracion():
    return render_template('admin.html')

@app.route('/comprobar.html', methods=['post','get'])
def comprobar():
    usuario = request.form["usuario"]
    contrasenia = request.form["contrasenia"]
    if(usuario=="GOD" and contrasenia=="KCHAME"):
        return render_template('admin.html')
    else:
        return render_template('login.html')

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

@app.route('/registros.html')
def registros():
    venta = obtener_ventas()
    return render_template("registros.html",venta=venta) 

@app.route('/limpiarcarrito.html', methods=["post"])
def limpiarcarrito():
    limpiar_carrito()
    return render_template("carrito.html")
numventa=1
@app.route('/pagarcarrito', methods=["post"])
def pagarcarrito():
    global numventa
    carrito = obtener_carrito()
    productos = obtener_productos()
    precio_total = 0
    for p in carrito:
        precio_total += int(p[4])

    pago = int(request.form["pago"])
    nombre= request.form["nombre"]
    productos_totales= ""
    cantidad_pedidos = [0,0,0,0,0,0,0,0,0]
    cantidad_productos = [0,0,0,0,0,0,0,0,0]
    if(pago >= precio_total ):
        numventa=numventa+1
        for p in carrito:
            productos_totales= productos_totales+str(p[2])+" "+ "producto "+", "
            cantidad_pedidos[p[0]] = p[2]
        for p in productos:
            cantidad_productos[p[0]] = p[3]

        cursor.execute("INSERT INTO ventas(idventa, comprador,producto,precio_total) VALUES(%s,%s,%s,%s)",(numventa,nombre,productos_totales,precio_total))
        connection.commit()    
        
        for i in range(1,9):
            cantidad_productos[i] -= cantidad_pedidos[i]
            cursor.execute("UPDATE `productosdb`.`productos` SET `cantidad` = '%s' WHERE (`idproductos` = '%s')",(cantidad_productos[i],i))
            connection.commit()
        limpiar_carrito()
        return render_template("pago_exitoso.html") 
    else:
        return render_template("pago_fallido.html")

#
## Agregandop1
vecesp1=1
aux1=0
cantstock=0
@app.route('/agregandop1.html',methods=["post"])
def agregandoP1():
    global vecesp1
    global cantstock
    global aux1
    cantidad=int(request.form["cantidad1"])
    precio=62.99
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Bugs Bunny"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==1):
            cantstock= int(p[3])
    if(cantstock>=cantidad):
        if(vecesp1==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(1,nombre,cantidad,precio,precio_t))
            vecesp1=vecesp1+1     
        if(vecesp1>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '1')",(cantidad+aux1))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '1')",(precio_t))
            connection.commit()
        aux1=aux1+cantidad
    return redirect("/index.html")

## Agregandop2
vecesp2=1
aux2=0
cantstock2=0
@app.route('/agregandop2.html',methods=["post"])
def agregandoP2():
    global vecesp2
    global cantstock2
    global aux2
    cantidad=int(request.form["cantidad2"])
    precio=65
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Pato Lucas"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==2):
            cantstock2= int(p[3])
    if(cantstock2>=cantidad):
        if(vecesp2==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(2,nombre,cantidad,precio,precio_t))
            connection.commit()
            vecesp2=vecesp2+1     
        if(vecesp2>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '2')",(cantidad+aux2))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '2')",(precio_t))
            connection.commit()
    aux2=aux2+cantidad
    return redirect("/index.html")

## Agregandop3
vecesp3=1
aux3=0
cantstock3=0
@app.route('/agregandop3.html',methods=["post"])
def agregandoP3():
    global vecesp3
    global cantstock3
    global aux3
    cantidad=int(request.form["cantidad3"])
    precio=79.99
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Taz"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==3):
            cantstock3= int(p[3])
    if(cantstock3>=cantidad):
        if(vecesp3==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(3,nombre,cantidad,precio,precio_t))
            connection.commit()
            vecesp3=vecesp3+1     
        if(vecesp3>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '3')",(cantidad+aux3))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '3')",(precio_t))
            connection.commit()
    aux3=aux3+cantidad
    return redirect("/index.html")

## Agregandop4
vecesp4=1
aux4=0
cantstock4=0
@app.route('/agregandop4.html',methods=["post"])
def agregandoP4():
    global vecesp4
    global cantstock4
    global aux4
    cantidad=int(request.form["cantidad4"])
    precio=59.99
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Marvin the martian"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==4):
            cantstock4= int(p[3])
    if(cantstock4>=cantidad):
        if(vecesp4==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(4,nombre,cantidad,precio,precio_t))
            connection.commit()
            vecesp4=vecesp4+1     
        if(vecesp4>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '4')",(cantidad+aux4))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '4')",(precio_t))
            connection.commit()
    aux4=aux4+cantidad
    return redirect("/index.html")

## Agregandop5
vecesp5=1
aux5=0
cantstock5=0
@app.route('/agregandop5.html',methods=["post"])
def agregandoP5():
    global vecesp5
    global cantstock5
    global aux5
    cantidad=int(request.form["cantidad5"])
    precio=99.99
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Porky Pig"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==5):
            cantstock5= int(p[3])
    if(cantstock5>=cantidad):
        if(vecesp5==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(5,nombre,cantidad,precio,precio_t))
            connection.commit()
            vecesp5=vecesp5+1     
        if(vecesp5>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '5')",(cantidad+aux5))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '5')",(precio_t))
            connection.commit()
    aux5=aux5+cantidad
    return redirect("/index.html")

## Agregandop6
vecesp6=1
aux6=0
cantstock6=0
@app.route('/agregandop6.html',methods=["post"])
def agregandoP6():
    global vecesp6
    global cantstock6
    global aux6
    cantidad=int(request.form["cantidad6"])
    precio=39.99
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Silvestre y Piolin"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==6):
            cantstock6= int(p[3])
    if(cantstock6>=cantidad):
        if(vecesp6==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(6,nombre,cantidad,precio,precio_t))
            connection.commit()
            vecesp6=vecesp6+1     
        if(vecesp6>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '6')",(cantidad+aux6))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '6')",(precio_t))
            connection.commit()
    aux6=aux6+cantidad
    return redirect("/index.html")

## Agregandop7
vecesp7=1
aux7=0
cantstock7=0
@app.route('/agregandop7.html',methods=["post"])
def agregandoP7():
    global vecesp7
    global cantstock7
    global aux7
    cantidad=int(request.form["cantidad7"])
    precio=69.99
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Swackhammer"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==7):
            cantstock7= int(p[3])
    if(cantstock7>=cantidad):
        if(vecesp7==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(7,nombre,cantidad,precio,precio_t))
            connection.commit()
            vecesp7=vecesp7+1     
        if(vecesp7>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '7')",(cantidad+aux7))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '7')",(precio_t))
            connection.commit()
    aux7=aux7+cantidad
    return redirect("/index.html")

## Agregandop8
vecesp8=1
aux8=0
cantstock8=0
@app.route('/agregandop8.html',methods=["post"])
def agregandoP8():
    global vecesp8
    global cantstock8
    global aux8
    cantidad=int(request.form["cantidad8"])
    precio=49.99
    precio_t=int(cantidad)*precio
    nombre="Funko POP Space Jam Viny"
    productos=obtener_productos()
    for p in productos:
        if(int(p[0])==8):
            cantstock8= int(p[3])
    if(cantstock8>=cantidad):
        if(vecesp8==1):
            cursor.execute("INSERT INTO carrito(idproducto, producto,cantidad,precio,precio_total) VALUES(%s,%s,%s,%s,%s)",(8,nombre,cantidad,precio,precio_t))
            connection.commit()
            vecesp8=vecesp8+1     
        if(vecesp8>1):
            cursor.execute("UPDATE `productosdb`.`carrito` SET `cantidad` = '%s' WHERE (`idproducto` = '8')",(cantidad+aux8))
            precio_t=int(cantidad)*precio
            cursor.execute("UPDATE `productosdb`.`carrito` SET `precio_total` = '%s' WHERE (`idproducto` = '8')",(precio_t))
            connection.commit()
    aux8=aux8+cantidad
    return redirect("/index.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
