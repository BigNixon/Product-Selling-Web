#########1
#Clase venta

class venta:

    def __init__(self,prod,prec,cant):
        self.producto=prod
        self.precio=prec
        self.cantidad=cant
    
    def venta(self):
        pass

    def registro_venta(self):
        pass

#########2
#Clase pedidos

class pedidos:

    def __init__(self,prodx,cantx,numsol):
        self.productop=prodx
        self.cantidadp=cantx
        self.numero_deSoli=numsol
    
    def recibir_pedido(self):
        pass

    def registro_pedido(self):
        pass

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
        pass

    def retorno(self):
        pass

#########4
#Clase almacen

class almacen(venta,pedidos):

    def __init__(self,nomempx,direx,prody,precy,canty,pedz,prodz,cantz,numsolz):
        venta.__init__(prody,precy,canty)
        pedidos.__init__(pedz,prodz,cantz,numsolz)
        self.nombre_empresa=nomempx
        self.direccion_almacen=direx

    def venta(self):
        pass

    def recibir_pedido(self):
        pass

    def recibir_pago(self):
        pass

#########5
#Clase existencias

class existencias(producto):

    def __init__(self,prody,pricey,canty,idprody,nomy,precioy,proveedory,cantz):
        super().__init__(idprody,nomy,precioy,proveedory,cantz)
        self.producto_num=prody
        self.precio_producto=pricey
        self.cantidad_existencia=canty

    def registro_de_venta(self):
        pass

    def existencias(self):
        pass

#########6
#Clase inventario

class inventario(producto,pedidos):

    def __init__(self,numsoli,idprodz,nomz,precioz,proveedorz,cantw,pedw,prodw,cantv,numsolw):
        producto.__init__(idprodz,nomz,precioz,proveedorz,cantw)
        pedidos.__init__(pedw,prodw,cantv,numsolw)
        self.numero_solicitud=numsoli

    def registro_de_pedido(self):
        pass

    def existencias(self):
        pass     

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
        pass

    def precios_especiales(self):
        pass   

#######8
#Clase control

class control:

    def __init__(self,proddx):
        self.productos=proddx
    
    def mant_y_control(self):
        pass

    def actualizacion(self):
        pass

    def depuracion(self):
        pass

#########9
#Clase administrador

class administrador(control):

    def __init__(self,prov,proddz):
        super().__init__(proddz)
        self.proveedores=prov
          
    def mantenimiento_control(self):
        pass
    
    def compra(self):
        pass

    def pedido(self):
        pass


