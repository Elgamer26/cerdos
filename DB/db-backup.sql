-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: Amadangelica1.mysql.pythonanywhere-services.com    Database: Amadangelica1$cerdos
-- ------------------------------------------------------
-- Server version	5.7.41-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alimentacion`
--

DROP TABLE IF EXISTS `alimentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimentacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alimento_id` int(11) DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `cantidad` int(11) DEFAULT NULL,
  `observacion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `semana` int(11) DEFAULT NULL,
  `id_cerdo` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `alimento_id` (`alimento_id`) USING BTREE,
  KEY `tipo_id` (`tipo_id`) USING BTREE,
  KEY `usuario_id` (`usuario_id`) USING BTREE,
  KEY `id_cerdo` (`id_cerdo`) USING BTREE,
  CONSTRAINT `alimentacion_ibfk_1` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimentacion_ibfk_2` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_alimentcion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimentacion_ibfk_3` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alimentacion`
--

LOCK TABLES `alimentacion` WRITE;
/*!40000 ALTER TABLE `alimentacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `alimentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alimento`
--

DROP TABLE IF EXISTS `alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `codigo` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `marca_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT '1',
  `precio` decimal(10,2) DEFAULT NULL,
  `peso` int(11) DEFAULT NULL,
  `detalle` text COLLATE utf8_spanish_ci,
  `foto` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tipo_id` (`tipo_id`) USING BTREE,
  KEY `marca_id` (`marca_id`) USING BTREE,
  CONSTRAINT `alimento_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimento_ibfk_2` FOREIGN KEY (`marca_id`) REFERENCES `marca_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alimento`
--

LOCK TABLES `alimento` WRITE;
/*!40000 ALTER TABLE `alimento` DISABLE KEYS */;
INSERT INTO `alimento` VALUES (6,'34927','ALCON CERDO PREINICIAL Fase 1',7,6,1,15.00,20,' Alimento balanceado para cerdos bebé, previo al destete.','20230201142048_Alcon cerdo preinicial.jpg',1),(7,'93574','ALCON CERDO PREINICIAL fase 2',7,6,1,16.00,20,' Alimento balanceado para verdos bebé, después del destete.','20230201142233_imagen_2023-02-01_092207952.png',1),(8,'47104','ALCON CERDOS INICIAL 18%',7,6,1,20.00,40,' Alimento balanceado para cerdos que inicial la etapa de engorde, potencializando el vigor de la raza.','20230201142423_imagen_2023-02-01_092414859.png',1),(9,'77462','ALCON CERDOS CRECIMIENTO 16%',7,6,1,30.00,40,' Alimento Balanceado para cerdos en la etapa de crecimiento. Brinda un aumento de tamaño.','20230201142532_imagen_2023-02-01_092531101.png',1),(10,'46235','ALCON CERDOS ACABADO 14%',7,6,1,28.00,40,'Alimento Balanceado para cerdos en la etapa de finalización, dando mayor peso y menor cantidad de grasa. ','20230201142647_imagen_2023-02-01_092642864.png',1),(11,'97272','ALCON CERDAS GESTANTES',7,6,1,30.00,40,'Alimento balanceado para cerdas preñadas, contribuyendo a tener lechones más grandes. ','20230201142814_imagen_2023-02-01_092810015.png',1),(12,'89119','ALCON CERDA LACTANTE',7,6,1,35.00,40,' Alimento balanceado para cerdas paridas, ayudando a tener mayor producción de leche.','20230201142911_imagen_2023-02-01_092910723.png',1);
/*!40000 ALTER TABLE `alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calendario`
--

DROP TABLE IF EXISTS `calendario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `calendario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `descripcion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `start` date DEFAULT NULL,
  `color` char(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `textColor` char(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `galpon_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `galpon_id` (`galpon_id`) USING BTREE,
  CONSTRAINT `calendario_ibfk_2` FOREIGN KEY (`galpon_id`) REFERENCES `galpon_cerdo_new` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calendario`
--

LOCK TABLES `calendario` WRITE;
/*!40000 ALTER TABLE `calendario` DISABLE KEYS */;
INSERT INTO `calendario` VALUES (16,'desparacitación','enfermedad','2023-02-10','#ff0000','#915050','Desparasitación',1,5);
/*!40000 ALTER TABLE `calendario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cerdo`
--

DROP TABLE IF EXISTS `cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cerdo` (
  `id_cerdo` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` char(25) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `sexo` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `raza` int(11) DEFAULT NULL,
  `peso` char(30) COLLATE utf8_spanish_ci DEFAULT NULL,
  `origen` text COLLATE utf8_spanish_ci,
  `fecha` date DEFAULT NULL,
  `detalle` text COLLATE utf8_spanish_ci,
  `foto` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `galpon` varchar(255) COLLATE utf8_spanish_ci DEFAULT 'no',
  `etapa` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_ingreso` char(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_cerdo`) USING BTREE,
  KEY `raza` (`raza`) USING BTREE,
  CONSTRAINT `cerdo_ibfk_1` FOREIGN KEY (`raza`) REFERENCES `raza` (`id_raza`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cerdo`
--

LOCK TABLES `cerdo` WRITE;
/*!40000 ALTER TABLE `cerdo` DISABLE KEYS */;
INSERT INTO `cerdo` VALUES (27,'2323','Dory','Macho',14,'2','Origen nacimiento.','2023-02-01',' Saludable.','cerdo.jpg',1,'si','Lactancia','Nacimiento',0.00),(53,'1234','PORKEY KING','Hembra',8,'3','Hacienda Amada Angelica','2022-12-14','CERDO MACHO PARA ENGORDE Y VENTA','cerdo.jpg',1,'no','Lactancia','Compra',100.00),(54,'4321','JACKS PARROU','Hembra',9,'3','Hacienda Amada Angelica','2022-12-14','CERDO EN BUEN ESTADO Y SALUD LISTO PARA CRIAR','cerdo.jpg',1,'no','Lactancia','Nacimiento',0.00),(55,'5678','PEDRO','Macho',10,'3','Hacienda Amada Angelica','2022-12-07','Detalle del cerdo','cerdo.jpg',1,'no','Lactancia','Compra',90.00),(56,'87654','DON CHANCHO','Hembra',11,'3','Hacienda Amada Angelica','2022-11-25','CERDO BLANCO QUE COME DE TODO Y ESTA BIEN GORDO','cerdo.jpg',1,'no','Lactancia','Nacimiento',0.00),(57,'7655','LA BICHOTA','Hembra',12,'3','Hacienda Amada Angelica','2022-09-01','Detalle del cerdo editado','cerdo.jpg',1,'no','Lactancia','Nacimiento',0.00);
/*!40000 ALTER TABLE `cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `apellidos` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `domicilio` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cedula` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `correo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra_alimento`
--

DROP TABLE IF EXISTS `compra_alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra_alimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) DEFAULT NULL,
  `proveedor_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `numero_compra` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `documento` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `iva` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `impuesto` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `usuario_id` (`usuario_id`) USING BTREE,
  KEY `proveedor_id` (`proveedor_id`) USING BTREE,
  CONSTRAINT `compra_alimento_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_alimento_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra_alimento`
--

LOCK TABLES `compra_alimento` WRITE;
/*!40000 ALTER TABLE `compra_alimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `compra_alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra_insumo`
--

DROP TABLE IF EXISTS `compra_insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra_insumo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) DEFAULT NULL,
  `proveedor_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `numero_compra` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `documento` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `iva` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `impuesto` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `usuario_id` (`usuario_id`) USING BTREE,
  KEY `proveedor_id` (`proveedor_id`) USING BTREE,
  CONSTRAINT `compra_insumo_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_insumo_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra_insumo`
--

LOCK TABLES `compra_insumo` WRITE;
/*!40000 ALTER TABLE `compra_insumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `compra_insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra_medicamento`
--

DROP TABLE IF EXISTS `compra_medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra_medicamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) DEFAULT NULL,
  `proveedor_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `numero_compra` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `documento` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `iva` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `impuesto` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `proveedor_id` (`proveedor_id`) USING BTREE,
  KEY `usuario_id` (`usuario_id`) USING BTREE,
  CONSTRAINT `compra_medicamento_ibfk_1` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_medicamento_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra_medicamento`
--

LOCK TABLES `compra_medicamento` WRITE;
/*!40000 ALTER TABLE `compra_medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `compra_medicamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compra_vacuna`
--

DROP TABLE IF EXISTS `compra_vacuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `compra_vacuna` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) DEFAULT NULL,
  `proveedor_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `numero_compra` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `documento` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `iva` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `impuesto` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `proveedor_id` (`proveedor_id`) USING BTREE,
  KEY `usuario_id` (`usuario_id`) USING BTREE,
  CONSTRAINT `compra_vacuna_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_vacuna_ibfk_3` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compra_vacuna`
--

LOCK TABLES `compra_vacuna` WRITE;
/*!40000 ALTER TABLE `compra_vacuna` DISABLE KEYS */;
/*!40000 ALTER TABLE `compra_vacuna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desparasitacion`
--

DROP TABLE IF EXISTS `desparasitacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desparasitacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medicamento_id` int(11) DEFAULT NULL,
  `semana` int(11) DEFAULT NULL,
  `cerdo_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `medicamento_id` (`medicamento_id`) USING BTREE,
  KEY `cerdo_id` (`cerdo_id`) USING BTREE,
  CONSTRAINT `desparasitacion_ibfk_1` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `desparasitacion_ibfk_2` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desparasitacion`
--

LOCK TABLES `desparasitacion` WRITE;
/*!40000 ALTER TABLE `desparasitacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `desparasitacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_alimentacion`
--

DROP TABLE IF EXISTS `detalle_alimentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_alimentacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_alimentacion` int(11) DEFAULT NULL,
  `id_cerdo` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id_alimentacion` (`id_alimentacion`) USING BTREE,
  KEY `id_cerdo` (`id_cerdo`) USING BTREE,
  CONSTRAINT `detalle_alimentacion_ibfk_1` FOREIGN KEY (`id_alimentacion`) REFERENCES `alimentacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_alimentacion_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_alimentacion`
--

LOCK TABLES `detalle_alimentacion` WRITE;
/*!40000 ALTER TABLE `detalle_alimentacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_alimentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_compra_alimento`
--

DROP TABLE IF EXISTS `detalle_compra_alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_compra_alimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compra_alimento_id` int(11) DEFAULT NULL,
  `alimento_id` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `descuento` int(11) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `compra_alimento_id` (`compra_alimento_id`) USING BTREE,
  KEY `alimento_id` (`alimento_id`) USING BTREE,
  CONSTRAINT `detalle_compra_alimento_ibfk_1` FOREIGN KEY (`compra_alimento_id`) REFERENCES `compra_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_alimento_ibfk_2` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_compra_alimento`
--

LOCK TABLES `detalle_compra_alimento` WRITE;
/*!40000 ALTER TABLE `detalle_compra_alimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_compra_alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_compra_insumo`
--

DROP TABLE IF EXISTS `detalle_compra_insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_compra_insumo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compra_insumo_id` int(11) DEFAULT NULL,
  `insumo_id` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `descuento` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `unidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `compra_insumo_id` (`compra_insumo_id`) USING BTREE,
  KEY `insumo_id` (`insumo_id`) USING BTREE,
  CONSTRAINT `detalle_compra_insumo_ibfk_1` FOREIGN KEY (`compra_insumo_id`) REFERENCES `compra_insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_insumo_ibfk_2` FOREIGN KEY (`insumo_id`) REFERENCES `insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_compra_insumo`
--

LOCK TABLES `detalle_compra_insumo` WRITE;
/*!40000 ALTER TABLE `detalle_compra_insumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_compra_insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_compra_medicamento`
--

DROP TABLE IF EXISTS `detalle_compra_medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_compra_medicamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compra_medicamento_id` int(11) DEFAULT NULL,
  `medicamento_id` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `descuento` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `unidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `compra_medicamento_id` (`compra_medicamento_id`) USING BTREE,
  KEY `medicamento_id` (`medicamento_id`) USING BTREE,
  CONSTRAINT `detalle_compra_medicamento_ibfk_1` FOREIGN KEY (`compra_medicamento_id`) REFERENCES `compra_medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_medicamento_ibfk_2` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_compra_medicamento`
--

LOCK TABLES `detalle_compra_medicamento` WRITE;
/*!40000 ALTER TABLE `detalle_compra_medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_compra_medicamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_compra_vacuna`
--

DROP TABLE IF EXISTS `detalle_compra_vacuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_compra_vacuna` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `compra_vacuna_id` int(11) DEFAULT NULL,
  `vacuna_id` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `descuento` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `compra_vacuna_id` (`compra_vacuna_id`) USING BTREE,
  KEY `vacuna_id` (`vacuna_id`) USING BTREE,
  CONSTRAINT `detalle_compra_vacuna_ibfk_1` FOREIGN KEY (`compra_vacuna_id`) REFERENCES `compra_vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_vacuna_ibfk_2` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_compra_vacuna`
--

LOCK TABLES `detalle_compra_vacuna` WRITE;
/*!40000 ALTER TABLE `detalle_compra_vacuna` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_compra_vacuna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_enfermedad_cerdo`
--

DROP TABLE IF EXISTS `detalle_enfermedad_cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_enfermedad_cerdo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cerdo_enfermedad_id` int(11) DEFAULT NULL,
  `enfermedad_id` int(11) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cerdo_enfermedad_id` (`cerdo_enfermedad_id`) USING BTREE,
  KEY `enfermedad_id` (`enfermedad_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_cerdo_ibfk_1` FOREIGN KEY (`cerdo_enfermedad_id`) REFERENCES `enfermedad_cerdo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_cerdo_ibfk_2` FOREIGN KEY (`enfermedad_id`) REFERENCES `enfermedad` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_enfermedad_cerdo`
--

LOCK TABLES `detalle_enfermedad_cerdo` WRITE;
/*!40000 ALTER TABLE `detalle_enfermedad_cerdo` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_enfermedad_cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_enfermedad_insumo`
--

DROP TABLE IF EXISTS `detalle_enfermedad_insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_enfermedad_insumo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tratamiento_id` int(11) DEFAULT NULL,
  `insumo_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tratamiento_id` (`tratamiento_id`) USING BTREE,
  KEY `insumo_id` (`insumo_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_insumo_ibfk_1` FOREIGN KEY (`tratamiento_id`) REFERENCES `tratamiento_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_insumo_ibfk_2` FOREIGN KEY (`insumo_id`) REFERENCES `insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_enfermedad_insumo`
--

LOCK TABLES `detalle_enfermedad_insumo` WRITE;
/*!40000 ALTER TABLE `detalle_enfermedad_insumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_enfermedad_insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_enfermedad_medicina`
--

DROP TABLE IF EXISTS `detalle_enfermedad_medicina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_enfermedad_medicina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trata_id` int(11) DEFAULT NULL,
  `medicina_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tratamiento_id` (`trata_id`) USING BTREE,
  KEY `medicina_id` (`medicina_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_medicina_ibfk_1` FOREIGN KEY (`trata_id`) REFERENCES `tratamiento_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_medicina_ibfk_2` FOREIGN KEY (`medicina_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_enfermedad_medicina`
--

LOCK TABLES `detalle_enfermedad_medicina` WRITE;
/*!40000 ALTER TABLE `detalle_enfermedad_medicina` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_enfermedad_medicina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_enfermedad_tratmiento`
--

DROP TABLE IF EXISTS `detalle_enfermedad_tratmiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_enfermedad_tratmiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tratamiento_id` int(11) DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tratamiento_id` (`tratamiento_id`) USING BTREE,
  KEY `tipo_id` (`tipo_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_tratmiento_ibfk_1` FOREIGN KEY (`tratamiento_id`) REFERENCES `tratamiento_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_tratmiento_ibfk_2` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_tratamiento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_enfermedad_tratmiento`
--

LOCK TABLES `detalle_enfermedad_tratmiento` WRITE;
/*!40000 ALTER TABLE `detalle_enfermedad_tratmiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_enfermedad_tratmiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_pedido_cerdo`
--

DROP TABLE IF EXISTS `detalle_pedido_cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_pedido_cerdo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_pedido` int(11) DEFAULT NULL,
  `id_cerdo` int(11) DEFAULT NULL,
  `peso` char(20) COLLATE utf8_spanish_ci DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id_pedido` (`id_pedido`) USING BTREE,
  KEY `id_cerdo` (`id_cerdo`) USING BTREE,
  CONSTRAINT `detalle_pedido_cerdo_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos_cerdo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_pedido_cerdo_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_pedido_cerdo`
--

LOCK TABLES `detalle_pedido_cerdo` WRITE;
/*!40000 ALTER TABLE `detalle_pedido_cerdo` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_pedido_cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_vacunacion`
--

DROP TABLE IF EXISTS `detalle_vacunacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_vacunacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vacunacion_id` int(11) DEFAULT NULL,
  `vacuna_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `motivo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `vacunacion_id` (`vacunacion_id`) USING BTREE,
  KEY `vacuna_id` (`vacuna_id`) USING BTREE,
  CONSTRAINT `detalle_vacunacion_ibfk_1` FOREIGN KEY (`vacunacion_id`) REFERENCES `vacunacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_vacunacion_ibfk_2` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_vacunacion`
--

LOCK TABLES `detalle_vacunacion` WRITE;
/*!40000 ALTER TABLE `detalle_vacunacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_vacunacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalle_venta_cerdos`
--

DROP TABLE IF EXISTS `detalle_venta_cerdos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalle_venta_cerdos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_venta` int(11) DEFAULT NULL,
  `id_cerdo` int(11) DEFAULT NULL,
  `peso` char(40) COLLATE utf8_spanish_ci DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id_venta` (`id_venta`) USING BTREE,
  KEY `id_cerdo` (`id_cerdo`) USING BTREE,
  CONSTRAINT `detalle_venta_cerdos_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_venta_cerdos_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalle_venta_cerdos`
--

LOCK TABLES `detalle_venta_cerdos` WRITE;
/*!40000 ALTER TABLE `detalle_venta_cerdos` DISABLE KEYS */;
/*!40000 ALTER TABLE `detalle_venta_cerdos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detallegalpon_cerdo`
--

DROP TABLE IF EXISTS `detallegalpon_cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detallegalpon_cerdo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_galpon` int(11) DEFAULT NULL,
  `id_cerdo` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id_galpon` (`id_galpon`) USING BTREE,
  KEY `id_cerdo` (`id_cerdo`) USING BTREE,
  CONSTRAINT `detallegalpon_cerdo_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpon_cerdo_new` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detallegalpon_cerdo_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detallegalpon_cerdo`
--

LOCK TABLES `detallegalpon_cerdo` WRITE;
/*!40000 ALTER TABLE `detallegalpon_cerdo` DISABLE KEYS */;
INSERT INTO `detallegalpon_cerdo` VALUES (6,5,27,'2023-02-01');
/*!40000 ALTER TABLE `detallegalpon_cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `id_hacienda` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ruc` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `correo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `foto` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `encargado` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `descripcion` text COLLATE utf8_spanish_ci,
  `direccion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id_hacienda`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'Nombre de hacienda','0985906677','0940321854','elgamer-26@hotmail.com','20230102135754pigs1.jpg','Encargado','Descripción de hacienda','Dirección');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enfermedad`
--

DROP TABLE IF EXISTS `enfermedad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enfermedad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `descripcion` text COLLATE utf8_spanish_ci,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enfermedad`
--

LOCK TABLES `enfermedad` WRITE;
/*!40000 ALTER TABLE `enfermedad` DISABLE KEYS */;
/*!40000 ALTER TABLE `enfermedad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enfermedad_cerdo`
--

DROP TABLE IF EXISTS `enfermedad_cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enfermedad_cerdo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cerdo_id` int(11) DEFAULT NULL,
  `veterinario_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `sintomas` text COLLATE utf8_spanish_ci,
  `diagnostico` text COLLATE utf8_spanish_ci,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cerdo_id` (`cerdo_id`) USING BTREE,
  KEY `veterinario_id` (`veterinario_id`) USING BTREE,
  CONSTRAINT `enfermedad_cerdo_ibfk_1` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `enfermedad_cerdo_ibfk_2` FOREIGN KEY (`veterinario_id`) REFERENCES `veterinario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enfermedad_cerdo`
--

LOCK TABLES `enfermedad_cerdo` WRITE;
/*!40000 ALTER TABLE `enfermedad_cerdo` DISABLE KEYS */;
/*!40000 ALTER TABLE `enfermedad_cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `galpon`
--

DROP TABLE IF EXISTS `galpon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `galpon` (
  `id_galpon` int(11) NOT NULL AUTO_INCREMENT,
  `numero` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `id_tipo` int(11) DEFAULT NULL,
  `capacidad` int(11) DEFAULT NULL,
  `observacion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `disponible` int(11) DEFAULT '1',
  PRIMARY KEY (`id_galpon`) USING BTREE,
  KEY `id_tipo` (`id_tipo`) USING BTREE,
  CONSTRAINT `galpon_ibfk_1` FOREIGN KEY (`id_tipo`) REFERENCES `tipo_galpon` (`id_tipo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galpon`
--

LOCK TABLES `galpon` WRITE;
/*!40000 ALTER TABLE `galpon` DISABLE KEYS */;
INSERT INTO `galpon` VALUES (6,'21944',6,30,'.',1,0);
/*!40000 ALTER TABLE `galpon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `galpon_cerdo`
--

DROP TABLE IF EXISTS `galpon_cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `galpon_cerdo` (
  `id_galpon_cerdo` int(11) NOT NULL AUTO_INCREMENT,
  `id_galpon` int(11) DEFAULT NULL,
  `id_cerdo` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id_galpon_cerdo`) USING BTREE,
  KEY `id_galpon` (`id_galpon`) USING BTREE,
  KEY `id_cerdo` (`id_cerdo`) USING BTREE,
  CONSTRAINT `galpon_cerdo_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpon` (`id_galpon`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `galpon_cerdo_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galpon_cerdo`
--

LOCK TABLES `galpon_cerdo` WRITE;
/*!40000 ALTER TABLE `galpon_cerdo` DISABLE KEYS */;
/*!40000 ALTER TABLE `galpon_cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `galpon_cerdo_new`
--

DROP TABLE IF EXISTS `galpon_cerdo_new`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `galpon_cerdo_new` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_galpon` int(11) DEFAULT NULL,
  `fecha_i` date DEFAULT NULL,
  `fecha_f` date DEFAULT NULL,
  `semana` int(11) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id_galpon` (`id_galpon`) USING BTREE,
  CONSTRAINT `galpon_cerdo_new_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpon` (`id_galpon`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galpon_cerdo_new`
--

LOCK TABLES `galpon_cerdo_new` WRITE;
/*!40000 ALTER TABLE `galpon_cerdo_new` DISABLE KEYS */;
INSERT INTO `galpon_cerdo_new` VALUES (5,6,'2023-02-01','2023-07-01',22,1);
/*!40000 ALTER TABLE `galpon_cerdo_new` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insumo`
--

DROP TABLE IF EXISTS `insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insumo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `detalle` text COLLATE utf8_spanish_ci,
  `foto` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `presentacion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tipo_id` (`tipo_id`) USING BTREE,
  CONSTRAINT `insumo_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insumo`
--

LOCK TABLES `insumo` WRITE;
/*!40000 ALTER TABLE `insumo` DISABLE KEYS */;
INSERT INTO `insumo` VALUES (4,'57244','SUPLEGAN',5,1,15.00,' Antibiótico que actua como promotor de crecimiento en cerdos. Promotor de crecimiento, para mejorar la conversión alimenticia. Prevención y tratamiento de enfermedades entéricas, leptospirosis, ERC y Sinovitis Infecciosa Coadyuvante en el control de infecciones causadas por Escherichia coli (Bacteria).','20230201143246_imagen_2023-02-01_093243402.png',1,'25 kg, 500 g.'),(5,'49758','RECOMPHOS_B12',6,1,20.00,' Para deficiencias de fosforo, estados de desnutrición, anemia, debilidad, estrés y en la convalecencia de enfermedades que afecten a los animales.','20230201144649_imagen_2023-02-01_094647505.png',1,'250ml');
/*!40000 ALTER TABLE `insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lote_alimento`
--

DROP TABLE IF EXISTS `lote_alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lote_alimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alimento_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fecha_i` date DEFAULT NULL,
  `fecha_f` date DEFAULT NULL,
  `codigo` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `alimento_id` (`alimento_id`) USING BTREE,
  CONSTRAINT `lote_alimento_ibfk_1` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lote_alimento`
--

LOCK TABLES `lote_alimento` WRITE;
/*!40000 ALTER TABLE `lote_alimento` DISABLE KEYS */;
/*!40000 ALTER TABLE `lote_alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lote_insumo`
--

DROP TABLE IF EXISTS `lote_insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lote_insumo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `insumo_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fecha_i` date DEFAULT NULL,
  `fecha_f` date DEFAULT NULL,
  `codigo` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `insumo_id` (`insumo_id`) USING BTREE,
  CONSTRAINT `lote_insumo_ibfk_1` FOREIGN KEY (`insumo_id`) REFERENCES `insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lote_insumo`
--

LOCK TABLES `lote_insumo` WRITE;
/*!40000 ALTER TABLE `lote_insumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `lote_insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lote_medicamento`
--

DROP TABLE IF EXISTS `lote_medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lote_medicamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `medicamento_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fecha_i` date DEFAULT NULL,
  `fecha_f` date DEFAULT NULL,
  `codigo` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `medicamento_id` (`medicamento_id`) USING BTREE,
  CONSTRAINT `lote_medicamento_ibfk_1` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lote_medicamento`
--

LOCK TABLES `lote_medicamento` WRITE;
/*!40000 ALTER TABLE `lote_medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `lote_medicamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lote_vacuna`
--

DROP TABLE IF EXISTS `lote_vacuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lote_vacuna` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vacuna_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `fecha_i` date DEFAULT NULL,
  `fecha_f` date DEFAULT NULL,
  `codigo` char(40) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `vacuna_id` (`vacuna_id`) USING BTREE,
  CONSTRAINT `lote_vacuna_ibfk_1` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lote_vacuna`
--

LOCK TABLES `lote_vacuna` WRITE;
/*!40000 ALTER TABLE `lote_vacuna` DISABLE KEYS */;
/*!40000 ALTER TABLE `lote_vacuna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marca_alimento`
--

DROP TABLE IF EXISTS `marca_alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca_alimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `marca_alimento` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca_alimento`
--

LOCK TABLES `marca_alimento` WRITE;
/*!40000 ALTER TABLE `marca_alimento` DISABLE KEYS */;
INSERT INTO `marca_alimento` VALUES (6,'Alcon',1);
/*!40000 ALTER TABLE `marca_alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicamento`
--

DROP TABLE IF EXISTS `medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT '0',
  `precio` decimal(10,2) DEFAULT NULL,
  `detalle` text COLLATE utf8_spanish_ci,
  `foto` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `presentacion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `unidades` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tipo_id` (`tipo_id`) USING BTREE,
  CONSTRAINT `medicamento_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicamento`
--

LOCK TABLES `medicamento` WRITE;
/*!40000 ALTER TABLE `medicamento` DISABLE KEYS */;
INSERT INTO `medicamento` VALUES (7,'21541','ACRILAN',4,1,10.00,' Cicatrizante para toda clase de heridas en animales.','20230201144121_imagen_2023-02-01_094119347.png',1,'50 g',1),(8,'33420','ACID – PAK 4 – WAY W.S. 2X',5,1,20.00,'Acidificador orgánico para suministrar en el agua de bebida para terneros y cerdos. ','20230201144233_imagen_2023-02-01_094230905.png',1,'1kg',1),(9,'38253','POMADA PARA UBRE',6,1,23.00,' Anti-inflamatorio para la ubre de las vacas y cerdas en producción. Actua como cicatrizante.','20230201144402_imagen_2023-02-01_094400128.png',1,'200g',1);
/*!40000 ALTER TABLE `medicamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimientos`
--

DROP TABLE IF EXISTS `movimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimientos` (
  `id_m` int(11) NOT NULL AUTO_INCREMENT,
  `id_g_c` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hasta` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id_m`) USING BTREE,
  KEY `id_g_c` (`id_g_c`) USING BTREE,
  CONSTRAINT `movimientos_ibfk_1` FOREIGN KEY (`id_g_c`) REFERENCES `galpon_cerdo` (`id_galpon_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimientos`
--

LOCK TABLES `movimientos` WRITE;
/*!40000 ALTER TABLE `movimientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `movimientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `muertes`
--

DROP TABLE IF EXISTS `muertes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `muertes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_cerdo` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `motivo` text COLLATE utf8_spanish_ci,
  `id_galpon` int(11) DEFAULT '1',
  `hora` time DEFAULT NULL,
  `semana` int(11) DEFAULT NULL,
  `f_registro` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `id_cerdo` (`id_cerdo`) USING BTREE,
  CONSTRAINT `muertes_ibfk_1` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `muertes`
--

LOCK TABLES `muertes` WRITE;
/*!40000 ALTER TABLE `muertes` DISABLE KEYS */;
/*!40000 ALTER TABLE `muertes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedidos_cerdo`
--

DROP TABLE IF EXISTS `pedidos_cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedidos_cerdo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `numero_pedido` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `apellido` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cedula` char(13) COLLATE utf8_spanish_ci DEFAULT NULL,
  `correo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `direccion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `impuesto` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '2',
  `iva` int(11) DEFAULT '12',
  `fecha_pedido` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedidos_cerdo`
--

LOCK TABLES `pedidos_cerdo` WRITE;
/*!40000 ALTER TABLE `pedidos_cerdo` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedidos_cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permisos`
--

DROP TABLE IF EXISTS `permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permisos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rol_id` int(11) DEFAULT NULL,
  `usuario` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `config` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cerdo` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `galpon` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `compra_venta` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `alimentacion` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `vacuna_despara` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `enfermedad_tratamiento` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  `informes` char(10) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `rol_id` (`rol_id`) USING BTREE,
  CONSTRAINT `permisos_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`rol_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permisos`
--

LOCK TABLES `permisos` WRITE;
/*!40000 ALTER TABLE `permisos` DISABLE KEYS */;
/*!40000 ALTER TABLE `permisos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `peso_cerdo`
--

DROP TABLE IF EXISTS `peso_cerdo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `peso_cerdo` (
  `peso_id` int(11) NOT NULL AUTO_INCREMENT,
  `cerdo_id` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `metodo` char(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `peso_pasado` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nuevo_pesaje` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `etapa_fase` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `perimetro_t` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `largo_c` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `observacion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `semana` int(11) DEFAULT NULL,
  PRIMARY KEY (`peso_id`) USING BTREE,
  KEY `cerdo_id` (`cerdo_id`) USING BTREE,
  CONSTRAINT `peso_cerdo_ibfk_1` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `peso_cerdo`
--

LOCK TABLES `peso_cerdo` WRITE;
/*!40000 ALTER TABLE `peso_cerdo` DISABLE KEYS */;
INSERT INTO `peso_cerdo` VALUES (25,27,'2023-02-01 15:33:59','vivo','2','2','Lactancia','30','40','a',1,1);
/*!40000 ALTER TABLE `peso_cerdo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedor`
--

DROP TABLE IF EXISTS `proveedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedor` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `razon` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ruc` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `correo` varchar(150) COLLATE utf8_spanish_ci DEFAULT NULL,
  `descripcion` text COLLATE utf8_spanish_ci,
  `encargado` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono_en` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `direccion` varchar(150) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedor`
--

LOCK TABLES `proveedor` WRITE;
/*!40000 ALTER TABLE `proveedor` DISABLE KEYS */;
INSERT INTO `proveedor` VALUES (2,'Agripac','0929604056001','0958993038','info@agripacc.com.ec','  Visión de consolidar al Grupo Corporativo en todo el territorio ecuatoriano.','Manuel Bertran','0958993038','Guayaquil',1);
/*!40000 ALTER TABLE `proveedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raza`
--

DROP TABLE IF EXISTS `raza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `raza` (
  `id_raza` int(11) NOT NULL AUTO_INCREMENT,
  `raza` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id_raza`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raza`
--

LOCK TABLES `raza` WRITE;
/*!40000 ALTER TABLE `raza` DISABLE KEYS */;
INSERT INTO `raza` VALUES (8,'Hampshire',1),(9,'Yorkshire',1),(10,'Landrace',1),(11,'Poland China',1),(12,'Duroc',1),(13,'Large Black',1),(14,'Pietrain',1);
/*!40000 ALTER TABLE `raza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `rol_id` int(11) NOT NULL AUTO_INCREMENT,
  `rol` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`rol_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'Administrador',1),(10,'Alimentador',1),(11,'Vendedor',1);
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_alimentcion`
--

DROP TABLE IF EXISTS `tipo_alimentcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_alimentcion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_alimentcion`
--

LOCK TABLES `tipo_alimentcion` WRITE;
/*!40000 ALTER TABLE `tipo_alimentcion` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_alimentcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_alimento`
--

DROP TABLE IF EXISTS `tipo_alimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_alimento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_alimento` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_alimento`
--

LOCK TABLES `tipo_alimento` WRITE;
/*!40000 ALTER TABLE `tipo_alimento` DISABLE KEYS */;
INSERT INTO `tipo_alimento` VALUES (7,'Balanceado',1);
/*!40000 ALTER TABLE `tipo_alimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_galpon`
--

DROP TABLE IF EXISTS `tipo_galpon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_galpon` (
  `id_tipo` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_galpon` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id_tipo`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_galpon`
--

LOCK TABLES `tipo_galpon` WRITE;
/*!40000 ALTER TABLE `tipo_galpon` DISABLE KEYS */;
INSERT INTO `tipo_galpon` VALUES (6,'Iniciador',1),(7,'Traspaso',1);
/*!40000 ALTER TABLE `tipo_galpon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_insumo`
--

DROP TABLE IF EXISTS `tipo_insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_insumo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_insumo`
--

LOCK TABLES `tipo_insumo` WRITE;
/*!40000 ALTER TABLE `tipo_insumo` DISABLE KEYS */;
INSERT INTO `tipo_insumo` VALUES (5,'Antibiótico',1),(6,'Vitamina',1);
/*!40000 ALTER TABLE `tipo_insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_medicamento`
--

DROP TABLE IF EXISTS `tipo_medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_medicamento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_medicamento`
--

LOCK TABLES `tipo_medicamento` WRITE;
/*!40000 ALTER TABLE `tipo_medicamento` DISABLE KEYS */;
INSERT INTO `tipo_medicamento` VALUES (4,'Cicatrizante',1),(5,'Acidificador organico',1),(6,'Anti-inflamatorio',1),(7,'Desinfectante',1),(8,'Antihistamínico',0);
/*!40000 ALTER TABLE `tipo_medicamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_tratamiento`
--

DROP TABLE IF EXISTS `tipo_tratamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_tratamiento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `descripcion` text COLLATE utf8_spanish_ci,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_tratamiento`
--

LOCK TABLES `tipo_tratamiento` WRITE;
/*!40000 ALTER TABLE `tipo_tratamiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `tipo_tratamiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_vacuna`
--

DROP TABLE IF EXISTS `tipo_vacuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_vacuna` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_vacuna` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_vacuna`
--

LOCK TABLES `tipo_vacuna` WRITE;
/*!40000 ALTER TABLE `tipo_vacuna` DISABLE KEYS */;
INSERT INTO `tipo_vacuna` VALUES (4,'Antihistamínico',1);
/*!40000 ALTER TABLE `tipo_vacuna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tratamiento_cerdos`
--

DROP TABLE IF EXISTS `tratamiento_cerdos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tratamiento_cerdos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `enfer_cerdo_id` int(11) DEFAULT NULL,
  `peso` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha_i` date DEFAULT NULL,
  `fecha_f` date DEFAULT NULL,
  `observacion` text COLLATE utf8_spanish_ci,
  `estado` int(11) DEFAULT '1',
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `enfer_cerdo_id` (`enfer_cerdo_id`) USING BTREE,
  CONSTRAINT `tratamiento_cerdos_ibfk_1` FOREIGN KEY (`enfer_cerdo_id`) REFERENCES `enfermedad_cerdo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tratamiento_cerdos`
--

LOCK TABLES `tratamiento_cerdos` WRITE;
/*!40000 ALTER TABLE `tratamiento_cerdos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tratamiento_cerdos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `apellidos` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `usuario` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `passwordd` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `rol_id` int(11) DEFAULT NULL,
  `domicilio` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` varchar(200) COLLATE utf8_spanish_ci DEFAULT NULL,
  `foto` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `correo` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cedula` char(11) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`usuario_id`) USING BTREE,
  KEY `rol_id` (`rol_id`) USING BTREE,
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`rol_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'PORKY','CERDO','admin','123',1,'casa','123','user.png',1,'elgamer-26@hotmail.com','1234567891'),(9,'JOSEE','VILLACRES','asa','Jorge2´+',1,'asa','asas','user.png',1,'2elgamer-26@hotmail.com','1234567892'),(11,'JORGE','WONG','Jorge','Jorge12q,.',1,'MILAGRO','0987654321','user.png',1,'3elgamer-26@hotmail.com','1234567893'),(13,'LA ROSALIA','ROSA','AdminInsetech','W2K8eZ-iuRY/',10,'MILAGRO ','0940321854','user.png',1,'Telgamer-26@hotmail.com','1234567894'),(17,'DANIEL ','FLORES','Lokochon','Ooi6XcR8DWlb',10,'NARANJITO','6789012345','user.png',1,'detodo@hotmail.com','0940321854'),(18,'ALBERT','WESKER','mapache','Voc-m&B45CJM',11,'RACCONN CITY','0987654321','user.png',0,'computacioneinformaticauae@gmail.com','0941129603'),(19,'Jorge','Wong','jwong','&m+-Zt62bk5P',1,'Milagro','0958993038','user.png',1,'jorgewongplay@gmail.com','0929604056');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacuna`
--

DROP TABLE IF EXISTS `vacuna`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacuna` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codigo` char(100) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `detalle` text COLLATE utf8_spanish_ci,
  `presentacion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `foto` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  `registro_sani` varchar(150) COLLATE utf8_spanish_ci DEFAULT NULL,
  `cantidad_dosis` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `tipo_id` (`tipo_id`) USING BTREE,
  CONSTRAINT `vacuna_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacuna`
--

LOCK TABLES `vacuna` WRITE;
/*!40000 ALTER TABLE `vacuna` DISABLE KEYS */;
INSERT INTO `vacuna` VALUES (6,'58919','HISTAMINEX',4,1,15.00,' Antihistaminico de amplio espectro. solución inyectable intramuscular o intravenosa lenta de uso veterinario.','100ml','20230201144848_imagen_2023-02-01_094846488.png',1,'.',120);
/*!40000 ALTER TABLE `vacuna` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacunacion`
--

DROP TABLE IF EXISTS `vacunacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacunacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cerdo_id` int(11) DEFAULT NULL,
  `vacuna_id` int(11) DEFAULT NULL,
  `semana` int(11) DEFAULT NULL,
  `dosis` int(11) DEFAULT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cerdo_id` (`cerdo_id`) USING BTREE,
  KEY `vacuna_id` (`vacuna_id`) USING BTREE,
  CONSTRAINT `vacunacion_ibfk_1` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `vacunacion_ibfk_2` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacunacion`
--

LOCK TABLES `vacunacion` WRITE;
/*!40000 ALTER TABLE `vacunacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacunacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta_cerdos`
--

DROP TABLE IF EXISTS `venta_cerdos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta_cerdos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_id` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `numero_venta` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `documento` char(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `iva` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `impuesto` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE,
  KEY `cliente_id` (`cliente_id`) USING BTREE,
  CONSTRAINT `venta_cerdos_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta_cerdos`
--

LOCK TABLES `venta_cerdos` WRITE;
/*!40000 ALTER TABLE `venta_cerdos` DISABLE KEYS */;
/*!40000 ALTER TABLE `venta_cerdos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinario`
--

DROP TABLE IF EXISTS `veterinario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `apellido` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `documento` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` char(15) COLLATE utf8_spanish_ci DEFAULT NULL,
  `direccion` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `sucursal` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado` int(11) DEFAULT '1',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veterinario`
--

LOCK TABLES `veterinario` WRITE;
/*!40000 ALTER TABLE `veterinario` DISABLE KEYS */;
/*!40000 ALTER TABLE `veterinario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `web`
--

DROP TABLE IF EXISTS `web`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `web` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `foto1` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `foto2` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `foto3` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `detalle1` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `detalle2` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `detalle3` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci ROW_FORMAT=DYNAMIC;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `web`
--

LOCK TABLES `web` WRITE;
/*!40000 ALTER TABLE `web` DISABLE KEYS */;
INSERT INTO `web` VALUES (1,'202301021358261434829025827.jpg','20230102140509118159693_4384045835002731_5782836742516971640_n.jpg','20230102135821pigs1.jpg','Los mejores cerdos','La  mejor calidad de cerdo','Los cerdos son cerdos y ricos ');
/*!40000 ALTER TABLE `web` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-27  0:49:11
