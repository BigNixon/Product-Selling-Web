#########1
#Clase venta
from main import *

class venta:

    def __init__(self,prod,prec,cant):
        self.producto = prod
        self.precio=prec
        self.cantidad=cant
    
    def venta(self):
        print("Venta exitosa")

    def registro_venta(self):
        print("Venta registrada")

#########2
#Clase pedidos

class pedidos:

    def __init__(self,prodx,cantx,numsol):
        self.productop=prodx
        self.cantidadp=cantx
        self.numero_deSoli=numsol
    
    def recibir_pedido(self):
        print("Pedido recibido")

    def registro_pedido(self):
        print("Pedido registrado")

#########3
#Clase producto

class producto:

    def __init__(self,idprod,nomx,preciox,proveedorx,cantx):
        self.id_producto=idprod
        self.nombre_producto=nomx
        self.precio_prod=preciox
        self.proveedor=proveedorx
        self.cantidad=cantx
    
    def asignacion(self):
        return "INSERT INTO productos(idproductos, nombre,precio,cantidad,proveedor) VALUES(%s,%s,%s,%s,%s)"

    def retorno(self):
        print("Devolviendo productos")

#########4
#Clase almacen

class almacen(venta,pedidos):

    def __init__(self,nomempx,direx,prody,precy,canty,pedz,prodz,cantz,numsolz):
        venta.__init__(prody,precy,canty)
        pedidos.__init__(pedz,prodz,cantz,numsolz)
        self.nombre_empresa=nomempx
        self.direccion_almacen=direx

    def venta(self):
        print("Venta exitosa")

    def recibir_pedido(self):
        print("Pedido recibido")

    def recibir_pago(self):
        print("Pago recibido")


#########5
#Clase existencias

class existencias(producto):

    def __init__(self,prody,pricey,canty,idprody,nomy,precioy,proveedory,cantz):
        super().__init__(idprody,nomy,precioy,proveedory,cantz)
        self.producto_num=prody
        self.precio_producto=pricey
        self.cantidad_existencia=canty

    def registro_de_venta(self):
        print("Venta Registrada")

    def existencias(self):
        print("Existencias")

#########6
#Clase inventario

class inventario(producto,pedidos):

    def __init__(self,numsoli,idprodz,nomz,precioz,proveedorz,cantw,pedw,prodw,cantv,numsolw):
        producto.__init__(idprodz,nomz,precioz,proveedorz,cantw)
        pedidos.__init__(pedw,prodw,cantv,numsolw)
        self.numero_solicitud=numsoli

    def registro_de_pedido(self):
        print("Registro de pedido")

    def existencias(self):
        print("Existencias")

#########7
#Clase proveedores

class proveedores:

    def __init__(self,telef,nt,dirx,cantx,prodx,nombre_prx):
        self.telefono=telef
        self.nit=nt
        self.direccion=dirx
        self.cantidad=cantx
        self.producto=prodx
        self.nombre_proveedor=nombre_prx
        
    def venta_directa(self):
        print("Venta directa")

    def pedidos_especiales(self):
        print("Pedidos especiales")
   

#######8
#Clase control

class control:

    def __init__(self,proddx):
        self.productos=proddx
    
    def mant_y_control(self):
        print("Mantenimiento")

    def actualizacion(self):
        print("Actualizacion")

    def depuracion(self):
        print("Depuracion")


#########9
#Clase administrador

class administrador(control):

    def __init__(self,prov,proddz):
        super().__init__(proddz)
        self.proveedores=prov
          
    def mantenimiento_control(self):
        print("Mantenimiento")
    
    def compra(self):
        print("compra")

    def pedido(self):
        print("pedido")



