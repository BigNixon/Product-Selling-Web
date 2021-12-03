create database productosDB;


############### CREACION DE LA TABLA PRODUCTOS ###########################
CREATE TABLE `productosdb`.`productos` (
  `idproductos` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `precio` INT NOT NULL,
  `cantidad` INT NOT NULL,
  `proveedor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idproductos`));
  
  #AÑADIENDO PRODUCTOS
		INSERT INTO `productosdb`.`productos` (`idproductos`, `nombre`, `precio`, `cantidad`, `proveedor`) VALUES ('1', 'funko1', '59', '20', 'china');
		INSERT INTO `productosdb`.`productos` (`idproductos`, `nombre`, `precio`, `cantidad`, `proveedor`) VALUES ('2', 'luffy', '75', '50', 'taiwan');


################### CREACION DE LA TABLA REGISTROS ############################
CREATE TABLE `productosdb`.`registro_ventas` (
  `idventa` INT NOT NULL AUTO_INCREMENT,
  `comprador` VARCHAR(45) NOT NULL,
  `destino` VARCHAR(45) NOT NULL,
  `idproductos` INT NOT NULL,
  PRIMARY KEY (`idventa`),
  INDEX `fk_idproductos_idx` (`idproductos` ASC) VISIBLE,
  CONSTRAINT `fk_idproductos`
    FOREIGN KEY (`idproductos`)
    REFERENCES `productosdb`.`productos` (`idproductos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

	#AÑADIENDO REGISTROS
    INSERT INTO `productosdb`.`registro_ventas` (`idventa`, `comprador`, `destino`, `idproductos`) VALUES ('1', 'marco', 'lima', '2');
	INSERT INTO `productosdb`.`registro_ventas` (`idventa`, `comprador`, `destino`, `idproductos`) VALUES ('2', 'elgod', 'callao', '1');

################ VISUALIZANDO LAS TABLAS #######################
SELECT * FROM	productos
SELECT * FROM	registro_ventas