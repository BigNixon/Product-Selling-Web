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
