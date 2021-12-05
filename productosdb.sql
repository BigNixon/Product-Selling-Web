create database productosdb;


############### CREACION DE LA TABLA PRODUCTOS ###########################
CREATE TABLE `productosdb`.`productos` (
  `idproductos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `precio` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `proveedor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idproductos`));

################### CREACION DE LA TABLA REGISTROS ############################
CREATE TABLE `productosdb`.`ventas` (
  `idventa` INT NOT NULL AUTO_INCREMENT,
  `comprador` VARCHAR(45) NOT NULL,
  `producto` VARCHAR(45) NOT NULL,
  `precio_total` INT NOT NULL,
  PRIMARY KEY (`idventa`));
  
								

################### CREACION DE LA TABLA carrito ############################
CREATE TABLE `productosdb`.`carrito` (
  `idproducto` INT NOT NULL AUTO_INCREMENT,
  `producto` VARCHAR(45) NOT NULL,
  `cantidad` INT NOT NULL,
  `precio` INT NOT NULL,
  `precio_total` INT NOT NULL,
  PRIMARY KEY (`idproducto`));
  

################ VISUALIZANDO LAS TABLAS #######################
#SELECT * FROM	productos;
#SELECT * FROM	registro_ventas;
DROP DATABASE productosdb