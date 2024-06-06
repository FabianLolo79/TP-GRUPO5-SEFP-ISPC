-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ColeccionDeVinilos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema ColeccionDeVinilos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ColeccionDeVinilos` DEFAULT CHARACTER SET utf8 ;
USE `ColeccionDeVinilos` ;

-- -----------------------------------------------------
-- Table `ColeccionDeVinilos`.`Artista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ColeccionDeVinilos`.`Artista` (
  `idArtista` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `Apellido` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idArtista`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ColeccionDeVinilos`.`Imagen_portada`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ColeccionDeVinilos`.`Imagen_portada` (
  `idImagen_portada` INT NOT NULL AUTO_INCREMENT,
  `Imagen_cara` VARCHAR(45) NULL,
  `Imagen_contraCara` VARCHAR(45) NULL,
  PRIMARY KEY (`idImagen_portada`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ColeccionDeVinilos`.`DiscoVinilo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ColeccionDeVinilos`.`DiscoVinilo` (
  `idDiscoVinilo` INT NOT NULL AUTO_INCREMENT,
  `Titulo` VARCHAR(45) NOT NULL,
  `Genero` VARCHAR(45) NULL,
  `Precio` FLOAT NULL,
  `anio` INT NULL,
  `idArtista` INT NOT NULL,
  `idImagen_portada` INT NOT NULL,
  PRIMARY KEY (`idDiscoVinilo`),
  INDEX `fk_DiscoVinilo_Artista1_idx` (`idArtista` ASC) VISIBLE,
  INDEX `fk_DiscoVinilo_Imagen_portada1_idx` (`idImagen_portada` ASC) VISIBLE,
  CONSTRAINT `fk_DiscoVinilo_Artista1`
    FOREIGN KEY (`idArtista`)
    REFERENCES `ColeccionDeVinilos`.`Artista` (`idArtista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DiscoVinilo_Imagen_portada1`
    FOREIGN KEY (`idImagen_portada`)
    REFERENCES `ColeccionDeVinilos`.`Imagen_portada` (`idImagen_portada`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ColeccionDeVinilos`.`Canciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `ColeccionDeVinilos`.`Canciones` (
  `idCanciones` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL,
  `Lado` VARCHAR(45) NULL,
  `idDiscoVinilo` INT NOT NULL,
  PRIMARY KEY (`idCanciones`),
  INDEX `fk_Canciones_DiscoVinilo1_idx` (`idDiscoVinilo` ASC) VISIBLE,
  CONSTRAINT `fk_Canciones_DiscoVinilo1`
    FOREIGN KEY (`idDiscoVinilo`)
    REFERENCES `ColeccionDeVinilos`.`DiscoVinilo` (`idDiscoVinilo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
