import pymysql
from flask.helpers import url_for
from flask import Flask, render_template,request,redirect,flash
from venta import *

# Conection with database
connection=pymysql.connect(
            host="127.0.0.1", # si es remota coloca dominio // local tu IP
            user='root',
            password='mypassword',
            db='productosdb',)

cursor = connection.cursor()


app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/carrito.html')
def carrito():
    return render_template('carrito.html')

@app.route('/admin.html')
def administracion():
    return render_template('admin.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)