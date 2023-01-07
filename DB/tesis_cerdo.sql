/*
 Navicat Premium Data Transfer

 Source Server         : Mysql
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : tesis_cerdo

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 07/01/2023 10:19:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alimentacion
-- ----------------------------
DROP TABLE IF EXISTS `alimentacion`;
CREATE TABLE `alimentacion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `alimento_id` int NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `usuario_id` int NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `cantidad` int NULL DEFAULT NULL,
  `observacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `semana` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `alimento_id`(`alimento_id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `alimentacion_ibfk_1` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimentacion_ibfk_2` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_alimentcion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimentacion_ibfk_3` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 46 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alimentacion
-- ----------------------------
INSERT INTO `alimentacion` VALUES (38, 2, 1, 1, '2022-12-08 17:49:23', 40, 'PARA  ENGORDA', 1, 1, 3);
INSERT INTO `alimentacion` VALUES (39, 2, 1, 1, '2022-12-08 18:03:48', 100, 'para engorda de los cerdos y salud', 1, 1, 3);
INSERT INTO `alimentacion` VALUES (40, 2, 1, 1, '2022-12-08 18:03:48', 100, 'para engorda de los cerdos y salud', 1, 1, 4);
INSERT INTO `alimentacion` VALUES (41, 2, 2, 1, '2022-12-08 18:22:19', 10, 'alimentación de salud', 1, 1, 4);
INSERT INTO `alimentacion` VALUES (42, 2, 2, 1, '2022-12-12 11:44:30', 5, 'para  salud del cerdo', 1, 2, 3);
INSERT INTO `alimentacion` VALUES (43, 2, 2, 1, '2022-12-12 11:44:30', 5, 'para  salud del cerdo', 1, 2, 4);
INSERT INTO `alimentacion` VALUES (44, 2, 1, 1, '2022-12-14 10:25:35', 1, 'PARA SALUD DEL CERDO', 1, 1, 5);
INSERT INTO `alimentacion` VALUES (45, 2, 2, 1, '2022-12-14 12:22:45', 2, 'PARA ENGORDA', 1, 1, 5);

-- ----------------------------
-- Table structure for alimento
-- ----------------------------
DROP TABLE IF EXISTS `alimento`;
CREATE TABLE `alimento`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `marca_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT 1,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `peso` int NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `foto` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  INDEX `marca_id`(`marca_id`) USING BTREE,
  CONSTRAINT `alimento_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `alimento_ibfk_2` FOREIGN KEY (`marca_id`) REFERENCES `marca_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alimento
-- ----------------------------
INSERT INTO `alimento` VALUES (1, '808715633', 'DON CHANCHO', 3, 2, 24, 24.00, 30, ' ALIMENTO PARA ENGORDA DEL CERDO Y PARA CRECIMIENTO', 'alimento.jpg', 1);
INSERT INTO `alimento` VALUES (2, '157962197', 'NUEVO ALIMENTO editaado', 2, 3, 68, 25.00, 35, ' Detalle del saco de alimento del cerdo editado ', 'alimento.jpg', 1);
INSERT INTO `alimento` VALUES (3, '888408884', 'Repuestos AlmaZull', 5, 4, 76, 23.00, 34, ' Detalle del saco de alimento del cerdo', 'alimento.jpg', 1);
INSERT INTO `alimento` VALUES (4, '69008286', 'BALANCEADOR ', 1, 1, 15, 30.00, 200, ' ALIMENTO PARA ENGORDA DE LOS CERDOS EN CRECIMIENTO', 'alimento.jpg', 1);
INSERT INTO `alimento` VALUES (5, '62452', 'BLUE GLASS EDIT', 3, 3, 21, 10.00, 300, ' Detalle del saco de alimento del cerdo', 'alimento.jpg', 1);

-- ----------------------------
-- Table structure for calendario
-- ----------------------------
DROP TABLE IF EXISTS `calendario`;
CREATE TABLE `calendario`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `start` date NULL DEFAULT NULL,
  `color` char(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `textColor` char(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `galpon_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `galpon_id`(`galpon_id`) USING BTREE,
  CONSTRAINT `calendario_ibfk_2` FOREIGN KEY (`galpon_id`) REFERENCES `galpon_cerdo_new` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of calendario
-- ----------------------------

-- ----------------------------
-- Table structure for cerdo
-- ----------------------------
DROP TABLE IF EXISTS `cerdo`;
CREATE TABLE `cerdo`  (
  `id_cerdo` int NOT NULL AUTO_INCREMENT,
  `codigo` char(25) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `sexo` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `raza` int NULL DEFAULT NULL,
  `peso` char(30) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `origen` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `fecha` date NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `galpon` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT 'no',
  `etapa` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo_ingreso` char(20) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `costo` decimal(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (`id_cerdo`) USING BTREE,
  INDEX `raza`(`raza`) USING BTREE,
  CONSTRAINT `cerdo_ibfk_1` FOREIGN KEY (`raza`) REFERENCES `raza` (`id_raza`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 22 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cerdo
-- ----------------------------
INSERT INTO `cerdo` VALUES (1, '964664418', 'pepe pig', 'Hembra', 2, '30', 'de la tev', '2022-11-10', ' en una cerdo bien sucia', 'cerdo.jpg', 2, 'si', 'Iniciador', 'Nacimiento', 0.00);
INSERT INTO `cerdo` VALUES (2, '964664411', 'pepe pig dos editado', 'Macho', 3, '25', 'Origen del cerdo editado', '2022-09-01', ' Detalle del cerdo editado', 'cerdo.jpg', 1, 'si', 'Iniciador', 'Nacimiento', 0.00);
INSERT INTO `cerdo` VALUES (3, '866533776', 'CERDO BLANCO DE A NIEVES', 'Hembra', 4, '50', 'LA GRANJA DE LA MONTAÑA', '2022-11-25', ' CERDO BLANCO QUE COME DE TODO Y ESTA BIEN GORDO', 'cerdo.jpg', 1, 'si', 'Crecimiento', 'Nacimiento', 0.00);
INSERT INTO `cerdo` VALUES (4, '46285', 'CHANCHITO', 'Macho', 1, '45', 'LA GRANJA DE LA MONTAÑA', '2022-12-07', ' Detalle del cerdo', 'cerdo.jpg', 1, 'si', 'Crecimiento', 'Compra', 800.00);
INSERT INTO `cerdo` VALUES (5, '2959', 'Black jack', 'Hembra', 7, '7', 'HACIENDA AMADA ANGELICA', '2022-12-14', ' CERDO EN BUEN ESTADO Y SALUD LISTO PARA CRIAR', 'cerdo.jpg', 1, 'si', 'Preiniciador', 'Nacimiento', 0.00);
INSERT INTO `cerdo` VALUES (6, '36339', 'KING PING', 'Macho', 6, '6', 'LA GRANJA DE LA MONTAÑA', '2022-12-14', ' CERDO MACHO PARA ENGORDE Y VENTA', 'cerdo.jpg', 1, 'no', 'Lactancia', 'Compra', 550.00);

-- ----------------------------
-- Table structure for cliente
-- ----------------------------
DROP TABLE IF EXISTS `cliente`;
CREATE TABLE `cliente`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `apellidos` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `domicilio` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `cedula` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `correo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cliente
-- ----------------------------
INSERT INTO `cliente` VALUES (1, 'JOSE JORGE', 'WONG VILLACRE', 'GUAYAQUIL', '01234567890', '0940321854', 'computacioneinformaticauae@gmail.com', 1);
INSERT INTO `cliente` VALUES (2, 'JOSE ALBERTH WESKER', 'ROJAS BLACK', 'MILAGRO AV SAN CARLOS', '0987654321', '0940321854001', 'ELGAMER-26@HOTMAIL.COM', 1);

-- ----------------------------
-- Table structure for compra_alimento
-- ----------------------------
DROP TABLE IF EXISTS `compra_alimento`;
CREATE TABLE `compra_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NULL DEFAULT NULL,
  `proveedor_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `numero_compra` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `iva` int NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  INDEX `proveedor_id`(`proveedor_id`) USING BTREE,
  CONSTRAINT `compra_alimento_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_alimento_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of compra_alimento
-- ----------------------------
INSERT INTO `compra_alimento` VALUES (9, 1, 1, '2022-09-25', '20220605190629', 'Factura', 12, 421.20, 50.54, 471.74, 0);
INSERT INTO `compra_alimento` VALUES (10, 1, 1, '2022-09-25', '20220605200640', 'nota_venta', 0, 36688.80, 0.00, 36688.80, 0);
INSERT INTO `compra_alimento` VALUES (11, 1, 1, '2022-09-26', '20220702090749', 'Factura', 12, 41698.80, 5003.86, 46702.66, 0);
INSERT INTO `compra_alimento` VALUES (30, 1, 1, '2022-12-04', '1234567', 'Factura', 12, 842.40, 101.09, 943.49, 1);
INSERT INTO `compra_alimento` VALUES (31, 1, 1, '2022-12-04', '12345321', 'Factura', 12, 19114.50, 2293.74, 21408.24, 1);

-- ----------------------------
-- Table structure for compra_insumo
-- ----------------------------
DROP TABLE IF EXISTS `compra_insumo`;
CREATE TABLE `compra_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NULL DEFAULT NULL,
  `proveedor_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `numero_compra` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `iva` int NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  INDEX `proveedor_id`(`proveedor_id`) USING BTREE,
  CONSTRAINT `compra_insumo_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_insumo_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of compra_insumo
-- ----------------------------
INSERT INTO `compra_insumo` VALUES (1, 1, 1, '2022-10-06', '20220605190634', 'Factura', 12, 321.00, 38.52, 359.52, 0);
INSERT INTO `compra_insumo` VALUES (2, 1, 1, '2022-10-06', '20220605190632', 'Factura', 12, 3318.00, 398.16, 3716.16, 0);
INSERT INTO `compra_insumo` VALUES (3, 1, 1, '2022-10-06', '20220605190609', 'Factura', 12, 3318.00, 398.16, 3716.16, 0);
INSERT INTO `compra_insumo` VALUES (4, 1, 1, '2022-10-06', '20220605190633', 'Factura', 12, 3330.00, 399.60, 3729.60, 0);
INSERT INTO `compra_insumo` VALUES (5, 1, 1, '2022-10-06', '20220605200640', 'Factura', 12, 3850.00, 462.00, 4312.00, 0);
INSERT INTO `compra_insumo` VALUES (6, 1, 1, '2022-10-06', '202206051906123', 'Factura', 12, 3318.00, 398.16, 3716.16, 0);
INSERT INTO `compra_insumo` VALUES (7, 1, 1, '2022-10-06', '20220605112345', 'Factura', 12, 333.00, 39.96, 372.96, 1);
INSERT INTO `compra_insumo` VALUES (8, 1, 1, '2022-10-06', '202206051954321', 'nota_venta', 0, 3330.00, 0.00, 3330.00, 1);
INSERT INTO `compra_insumo` VALUES (9, 1, 1, '2022-10-06', '202206052456', 'nota_venta', 0, 6993.00, 0.00, 6993.00, 1);
INSERT INTO `compra_insumo` VALUES (12, 1, 1, '2022-12-10', '20220605190321', 'Factura', 12, 60.50, 7.26, 67.76, 1);
INSERT INTO `compra_insumo` VALUES (13, 1, 1, '2022-12-10', '20220605203451', 'Factura', 12, 181.50, 21.78, 203.28, 1);
INSERT INTO `compra_insumo` VALUES (14, 1, 1, '2022-12-13', '121209090', 'Factura', 12, 120.50, 14.46, 134.96, 1);

-- ----------------------------
-- Table structure for compra_medicamento
-- ----------------------------
DROP TABLE IF EXISTS `compra_medicamento`;
CREATE TABLE `compra_medicamento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NULL DEFAULT NULL,
  `proveedor_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `numero_compra` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `iva` int NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `proveedor_id`(`proveedor_id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  CONSTRAINT `compra_medicamento_ibfk_1` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_medicamento_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of compra_medicamento
-- ----------------------------
INSERT INTO `compra_medicamento` VALUES (8, 1, 1, '2022-11-11', '20220605200640', 'Factura', 12, 12.00, 1.44, 13.44, 1);
INSERT INTO `compra_medicamento` VALUES (9, 1, 1, '2022-11-11', '20220702090749', 'Factura', 12, 120.00, 14.40, 134.40, 1);
INSERT INTO `compra_medicamento` VALUES (13, 1, 1, '2022-12-08', '20220605190634', 'Factura', 12, 60.00, 7.20, 67.20, 1);
INSERT INTO `compra_medicamento` VALUES (14, 1, 1, '2022-12-08', '202206012121', 'Factura', 12, 267.50, 32.10, 299.60, 1);
INSERT INTO `compra_medicamento` VALUES (15, 1, 1, '2022-12-12', '091212109', 'Factura', 12, 100.00, 12.00, 112.00, 1);

-- ----------------------------
-- Table structure for compra_vacuna
-- ----------------------------
DROP TABLE IF EXISTS `compra_vacuna`;
CREATE TABLE `compra_vacuna`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NULL DEFAULT NULL,
  `proveedor_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `numero_compra` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `iva` int NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `proveedor_id`(`proveedor_id`) USING BTREE,
  INDEX `usuario_id`(`usuario_id`) USING BTREE,
  CONSTRAINT `compra_vacuna_ibfk_2` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedor` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `compra_vacuna_ibfk_3` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of compra_vacuna
-- ----------------------------
INSERT INTO `compra_vacuna` VALUES (4, 1, 1, '2022-11-17', '20220605200640', 'Factura', 12, 950.00, 114.00, 1064.00, 0);
INSERT INTO `compra_vacuna` VALUES (5, 1, 1, '2022-11-18', '20220605190633', 'nota_venta', 0, 110.00, 0.00, 110.00, 0);
INSERT INTO `compra_vacuna` VALUES (6, 1, 1, '2022-12-03', '121222222221212', 'Factura', 12, 6300.00, 756.00, 7056.00, 1);
INSERT INTO `compra_vacuna` VALUES (7, 1, 1, '2022-12-03', '4562323244343', 'Factura', 12, 14000.00, 1680.00, 15680.00, 1);
INSERT INTO `compra_vacuna` VALUES (8, 1, 1, '2022-12-02', '098767890', 'Factura', 12, 34030.00, 4083.60, 38113.60, 1);
INSERT INTO `compra_vacuna` VALUES (9, 1, 1, '2022-12-04', '3233232', 'Factura', 12, 220.00, 26.40, 246.40, 1);

-- ----------------------------
-- Table structure for desparasitacion
-- ----------------------------
DROP TABLE IF EXISTS `desparasitacion`;
CREATE TABLE `desparasitacion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `medicamento_id` int NULL DEFAULT NULL,
  `semana` int NULL DEFAULT NULL,
  `cerdo_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `medicamento_id`(`medicamento_id`) USING BTREE,
  INDEX `cerdo_id`(`cerdo_id`) USING BTREE,
  CONSTRAINT `desparasitacion_ibfk_1` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `desparasitacion_ibfk_2` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of desparasitacion
-- ----------------------------
INSERT INTO `desparasitacion` VALUES (1, 4, 1, 3, 10, '2022-12-08 14:13:47');
INSERT INTO `desparasitacion` VALUES (2, 5, 1, 3, 20, '2022-12-08 14:36:19');
INSERT INTO `desparasitacion` VALUES (3, 4, 1, 4, 5, '2022-12-08 14:37:43');
INSERT INTO `desparasitacion` VALUES (4, 5, 1, 3, 15, '2022-12-08 15:21:24');
INSERT INTO `desparasitacion` VALUES (5, 5, 1, 4, 15, '2022-12-08 15:21:24');
INSERT INTO `desparasitacion` VALUES (6, 6, 2, 3, 2, '2022-12-12 15:23:44');
INSERT INTO `desparasitacion` VALUES (7, 6, 2, 4, 2, '2022-12-12 15:23:44');
INSERT INTO `desparasitacion` VALUES (8, 4, 1, 5, 1, '2022-12-14 12:21:56');
INSERT INTO `desparasitacion` VALUES (9, 4, 3, 3, 1, '2022-12-15 19:05:00');
INSERT INTO `desparasitacion` VALUES (10, 4, 3, 4, 1, '2022-12-15 19:05:00');
INSERT INTO `desparasitacion` VALUES (11, 4, 3, 3, 1, '2022-12-15 19:05:26');

-- ----------------------------
-- Table structure for detalle_alimentacion
-- ----------------------------
DROP TABLE IF EXISTS `detalle_alimentacion`;
CREATE TABLE `detalle_alimentacion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_alimentacion` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_alimentacion`(`id_alimentacion`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `detalle_alimentacion_ibfk_1` FOREIGN KEY (`id_alimentacion`) REFERENCES `alimentacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_alimentacion_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 37 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_alimentacion
-- ----------------------------

-- ----------------------------
-- Table structure for detalle_compra_alimento
-- ----------------------------
DROP TABLE IF EXISTS `detalle_compra_alimento`;
CREATE TABLE `detalle_compra_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `compra_alimento_id` int NULL DEFAULT NULL,
  `alimento_id` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `descuento` int NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `compra_alimento_id`(`compra_alimento_id`) USING BTREE,
  INDEX `alimento_id`(`alimento_id`) USING BTREE,
  CONSTRAINT `detalle_compra_alimento_ibfk_1` FOREIGN KEY (`compra_alimento_id`) REFERENCES `compra_alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_alimento_ibfk_2` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 38 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_compra_alimento
-- ----------------------------
INSERT INTO `detalle_compra_alimento` VALUES (1, 9, 1, 100.20, 1, 0, 100.20, 1);
INSERT INTO `detalle_compra_alimento` VALUES (2, 9, 2, 321.00, 1, 0, 321.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (3, 10, 1, 100.20, 49, 0, 4909.80, 1);
INSERT INTO `detalle_compra_alimento` VALUES (4, 10, 2, 321.00, 99, 0, 31779.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (5, 11, 1, 100.20, 99, 0, 9919.80, 1);
INSERT INTO `detalle_compra_alimento` VALUES (6, 11, 2, 321.00, 99, 0, 31779.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (31, 30, 1, 100.20, 2, 0, 200.40, 1);
INSERT INTO `detalle_compra_alimento` VALUES (32, 30, 2, 321.00, 2, 0, 642.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (33, 31, 1, 100.20, 10, 0, 1002.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (34, 31, 2, 321.00, 50, 0, 16050.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (35, 31, 3, 23.00, 70, 0, 1610.00, 1);
INSERT INTO `detalle_compra_alimento` VALUES (36, 31, 4, 50.50, 5, 0, 252.50, 1);
INSERT INTO `detalle_compra_alimento` VALUES (37, 31, 5, 10.00, 20, 0, 200.00, 1);

-- ----------------------------
-- Table structure for detalle_compra_insumo
-- ----------------------------
DROP TABLE IF EXISTS `detalle_compra_insumo`;
CREATE TABLE `detalle_compra_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `compra_insumo_id` int NULL DEFAULT NULL,
  `insumo_id` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `descuento` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `unidad` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `compra_insumo_id`(`compra_insumo_id`) USING BTREE,
  INDEX `insumo_id`(`insumo_id`) USING BTREE,
  CONSTRAINT `detalle_compra_insumo_ibfk_1` FOREIGN KEY (`compra_insumo_id`) REFERENCES `compra_insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_insumo_ibfk_2` FOREIGN KEY (`insumo_id`) REFERENCES `insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_compra_insumo
-- ----------------------------
INSERT INTO `detalle_compra_insumo` VALUES (1, 3, 1, 321.00, 10, 0.00, 3210.00, 0, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (2, 3, 2, 12.00, 9, 0.00, 108.00, 0, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (3, 4, 1, 321.00, 10, 0.00, 3210.00, 0, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (4, 4, 2, 12.00, 10, 0.00, 120.00, 0, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (5, 5, 1, 321.00, 12, 2.00, 3850.00, 0, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (6, 6, 2, 12.00, 9, 0.00, 108.00, 0, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (7, 6, 1, 321.00, 10, 0.00, 3210.00, 1, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (8, 7, 1, 321.00, 1, 0.00, 321.00, 1, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (9, 7, 2, 12.00, 1, 0.00, 12.00, 1, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (10, 8, 1, 321.00, 10, 0.00, 3210.00, 1, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (11, 8, 2, 12.00, 10, 0.00, 120.00, 1, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (12, 9, 1, 321.00, 21, 0.00, 6741.00, 1, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (13, 9, 2, 12.00, 21, 0.00, 252.00, 1, NULL);
INSERT INTO `detalle_compra_insumo` VALUES (14, 12, 1, 30.25, 2, 0.00, 60.50, 1, 10);
INSERT INTO `detalle_compra_insumo` VALUES (15, 13, 1, 30.25, 6, 0.00, 181.50, 1, 5);
INSERT INTO `detalle_compra_insumo` VALUES (16, 14, 1, 30.25, 2, 0.00, 60.50, 1, 5);
INSERT INTO `detalle_compra_insumo` VALUES (17, 14, 2, 12.00, 5, 0.00, 60.00, 1, 2);

-- ----------------------------
-- Table structure for detalle_compra_medicamento
-- ----------------------------
DROP TABLE IF EXISTS `detalle_compra_medicamento`;
CREATE TABLE `detalle_compra_medicamento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `compra_medicamento_id` int NULL DEFAULT NULL,
  `medicamento_id` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `descuento` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `unidad` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `compra_medicamento_id`(`compra_medicamento_id`) USING BTREE,
  INDEX `medicamento_id`(`medicamento_id`) USING BTREE,
  CONSTRAINT `detalle_compra_medicamento_ibfk_1` FOREIGN KEY (`compra_medicamento_id`) REFERENCES `compra_medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_medicamento_ibfk_2` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_compra_medicamento
-- ----------------------------
INSERT INTO `detalle_compra_medicamento` VALUES (13, 8, 4, 12.00, 1, 0.00, 12.00, 1, NULL);
INSERT INTO `detalle_compra_medicamento` VALUES (14, 9, 4, 12.00, 10, 0.00, 120.00, 1, NULL);
INSERT INTO `detalle_compra_medicamento` VALUES (15, 13, 4, 12.00, 5, 0.00, 60.00, 1, 10);
INSERT INTO `detalle_compra_medicamento` VALUES (16, 14, 4, 12.00, 5, 0.00, 60.00, 1, 10);
INSERT INTO `detalle_compra_medicamento` VALUES (17, 14, 5, 20.75, 10, 0.00, 207.50, 1, 5);
INSERT INTO `detalle_compra_medicamento` VALUES (18, 15, 6, 10.00, 10, 0.00, 100.00, 1, 5);

-- ----------------------------
-- Table structure for detalle_compra_vacuna
-- ----------------------------
DROP TABLE IF EXISTS `detalle_compra_vacuna`;
CREATE TABLE `detalle_compra_vacuna`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `compra_vacuna_id` int NULL DEFAULT NULL,
  `vacuna_id` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `descuento` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `compra_vacuna_id`(`compra_vacuna_id`) USING BTREE,
  INDEX `vacuna_id`(`vacuna_id`) USING BTREE,
  CONSTRAINT `detalle_compra_vacuna_ibfk_1` FOREIGN KEY (`compra_vacuna_id`) REFERENCES `compra_vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_compra_vacuna_ibfk_2` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_compra_vacuna
-- ----------------------------
INSERT INTO `detalle_compra_vacuna` VALUES (1, 4, 1, 10.00, 5, 0.00, 50.00, 0);
INSERT INTO `detalle_compra_vacuna` VALUES (2, 4, 2, 100.00, 9, 0.00, 900.00, 0);
INSERT INTO `detalle_compra_vacuna` VALUES (3, 5, 1, 10.00, 1, 0.00, 10.00, 0);
INSERT INTO `detalle_compra_vacuna` VALUES (4, 5, 2, 100.00, 1, 0.00, 100.00, 0);
INSERT INTO `detalle_compra_vacuna` VALUES (5, 6, 1, 10.00, 30, 0.00, 300.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (6, 6, 2, 100.00, 60, 0.00, 6000.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (7, 7, 1, 10.00, 500, 0.00, 5000.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (8, 7, 2, 100.00, 30, 0.00, 3000.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (9, 7, 3, 100.00, 60, 0.00, 6000.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (10, 8, 1, 10.00, 500, 0.00, 5000.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (11, 8, 2, 100.00, 50, 0.00, 5000.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (12, 8, 3, 100.00, 90, 0.00, 9000.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (13, 8, 4, 70.00, 123, 0.00, 8610.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (14, 8, 5, 20.00, 321, 0.00, 6420.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (15, 9, 1, 10.00, 2, 0.00, 20.00, 1);
INSERT INTO `detalle_compra_vacuna` VALUES (16, 9, 2, 100.00, 2, 0.00, 200.00, 1);

-- ----------------------------
-- Table structure for detalle_enfermedad_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `detalle_enfermedad_cerdo`;
CREATE TABLE `detalle_enfermedad_cerdo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `cerdo_enfermedad_id` int NULL DEFAULT NULL,
  `enfermedad_id` int NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cerdo_enfermedad_id`(`cerdo_enfermedad_id`) USING BTREE,
  INDEX `enfermedad_id`(`enfermedad_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_cerdo_ibfk_1` FOREIGN KEY (`cerdo_enfermedad_id`) REFERENCES `enfermedad_cerdo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_cerdo_ibfk_2` FOREIGN KEY (`enfermedad_id`) REFERENCES `enfermedad` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_enfermedad_cerdo
-- ----------------------------
INSERT INTO `detalle_enfermedad_cerdo` VALUES (6, 5, 1, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (7, 5, 2, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (8, 6, 1, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (9, 7, 2, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (10, 7, 1, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (11, 8, 1, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (12, 8, 2, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (16, 11, 1, 1);
INSERT INTO `detalle_enfermedad_cerdo` VALUES (17, 12, 1, 1);

-- ----------------------------
-- Table structure for detalle_enfermedad_insumo
-- ----------------------------
DROP TABLE IF EXISTS `detalle_enfermedad_insumo`;
CREATE TABLE `detalle_enfermedad_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tratamiento_id` int NULL DEFAULT NULL,
  `insumo_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tratamiento_id`(`tratamiento_id`) USING BTREE,
  INDEX `insumo_id`(`insumo_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_insumo_ibfk_1` FOREIGN KEY (`tratamiento_id`) REFERENCES `tratamiento_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_insumo_ibfk_2` FOREIGN KEY (`insumo_id`) REFERENCES `insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_enfermedad_insumo
-- ----------------------------
INSERT INTO `detalle_enfermedad_insumo` VALUES (12, 16, 1, 1);
INSERT INTO `detalle_enfermedad_insumo` VALUES (13, 17, 1, 1);
INSERT INTO `detalle_enfermedad_insumo` VALUES (14, 18, 1, 10);
INSERT INTO `detalle_enfermedad_insumo` VALUES (15, 18, 2, 10);
INSERT INTO `detalle_enfermedad_insumo` VALUES (16, 19, 1, 1);
INSERT INTO `detalle_enfermedad_insumo` VALUES (17, 19, 2, 1);

-- ----------------------------
-- Table structure for detalle_enfermedad_medicina
-- ----------------------------
DROP TABLE IF EXISTS `detalle_enfermedad_medicina`;
CREATE TABLE `detalle_enfermedad_medicina`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `trata_id` int NULL DEFAULT NULL,
  `medicina_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tratamiento_id`(`trata_id`) USING BTREE,
  INDEX `medicina_id`(`medicina_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_medicina_ibfk_1` FOREIGN KEY (`trata_id`) REFERENCES `tratamiento_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_medicina_ibfk_2` FOREIGN KEY (`medicina_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_enfermedad_medicina
-- ----------------------------
INSERT INTO `detalle_enfermedad_medicina` VALUES (9, 16, 4, 1);
INSERT INTO `detalle_enfermedad_medicina` VALUES (10, 17, 4, 1);
INSERT INTO `detalle_enfermedad_medicina` VALUES (11, 18, 4, 10);
INSERT INTO `detalle_enfermedad_medicina` VALUES (12, 19, 4, 5);

-- ----------------------------
-- Table structure for detalle_enfermedad_tratmiento
-- ----------------------------
DROP TABLE IF EXISTS `detalle_enfermedad_tratmiento`;
CREATE TABLE `detalle_enfermedad_tratmiento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tratamiento_id` int NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tratamiento_id`(`tratamiento_id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  CONSTRAINT `detalle_enfermedad_tratmiento_ibfk_1` FOREIGN KEY (`tratamiento_id`) REFERENCES `tratamiento_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_enfermedad_tratmiento_ibfk_2` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_tratamiento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_enfermedad_tratmiento
-- ----------------------------
INSERT INTO `detalle_enfermedad_tratmiento` VALUES (6, 16, 1);
INSERT INTO `detalle_enfermedad_tratmiento` VALUES (7, 16, 2);
INSERT INTO `detalle_enfermedad_tratmiento` VALUES (8, 17, 1);
INSERT INTO `detalle_enfermedad_tratmiento` VALUES (9, 17, 2);
INSERT INTO `detalle_enfermedad_tratmiento` VALUES (10, 18, 1);
INSERT INTO `detalle_enfermedad_tratmiento` VALUES (11, 19, 1);
INSERT INTO `detalle_enfermedad_tratmiento` VALUES (12, 19, 2);

-- ----------------------------
-- Table structure for detalle_pedido_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `detalle_pedido_cerdo`;
CREATE TABLE `detalle_pedido_cerdo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_pedido` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  `peso` char(20) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_pedido`(`id_pedido`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `detalle_pedido_cerdo_ibfk_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedidos_cerdo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_pedido_cerdo_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_pedido_cerdo
-- ----------------------------
INSERT INTO `detalle_pedido_cerdo` VALUES (1, 6, 2, '25', 5.00, 125.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (2, 6, 3, '50', 5.00, 250.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (3, 6, 4, '45', 5.00, 225.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (4, 7, 2, '25', 5.00, 125.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (5, 7, 3, '50', 5.00, 250.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (6, 8, 2, '25', 5.00, 125.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (7, 8, 3, '50', 5.00, 250.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (8, 9, 4, '45', 5.00, 225.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (9, 9, 5, '7', 5.00, 35.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (10, 10, 2, '25', 5.00, 125.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (11, 10, 5, '7', 5.00, 35.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (12, 11, 3, '50', 5.00, 250.00, 1);
INSERT INTO `detalle_pedido_cerdo` VALUES (13, 11, 4, '45', 5.00, 225.00, 1);

-- ----------------------------
-- Table structure for detalle_vacunacion
-- ----------------------------
DROP TABLE IF EXISTS `detalle_vacunacion`;
CREATE TABLE `detalle_vacunacion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `vacunacion_id` int NULL DEFAULT NULL,
  `vacuna_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `motivo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `vacunacion_id`(`vacunacion_id`) USING BTREE,
  INDEX `vacuna_id`(`vacuna_id`) USING BTREE,
  CONSTRAINT `detalle_vacunacion_ibfk_1` FOREIGN KEY (`vacunacion_id`) REFERENCES `vacunacion` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_vacunacion_ibfk_2` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_vacunacion
-- ----------------------------

-- ----------------------------
-- Table structure for detalle_venta_cerdos
-- ----------------------------
DROP TABLE IF EXISTS `detalle_venta_cerdos`;
CREATE TABLE `detalle_venta_cerdos`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_venta` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  `peso` char(40) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_venta`(`id_venta`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `detalle_venta_cerdos_ibfk_1` FOREIGN KEY (`id_venta`) REFERENCES `venta_cerdos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detalle_venta_cerdos_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detalle_venta_cerdos
-- ----------------------------
INSERT INTO `detalle_venta_cerdos` VALUES (1, 3, 2, '25', 1.00, 25.00, 1);
INSERT INTO `detalle_venta_cerdos` VALUES (2, 3, 3, '50', 2.00, 100.00, 1);
INSERT INTO `detalle_venta_cerdos` VALUES (3, 4, 5, '7', 120.00, 840.00, 1);
INSERT INTO `detalle_venta_cerdos` VALUES (4, 4, 2, '25', 199.00, 4975.00, 1);
INSERT INTO `detalle_venta_cerdos` VALUES (5, 5, 3, '50', 234.00, 11700.00, 1);

-- ----------------------------
-- Table structure for detallegalpon_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `detallegalpon_cerdo`;
CREATE TABLE `detallegalpon_cerdo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_galpon` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_galpon`(`id_galpon`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `detallegalpon_cerdo_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpon_cerdo_new` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `detallegalpon_cerdo_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of detallegalpon_cerdo
-- ----------------------------
INSERT INTO `detallegalpon_cerdo` VALUES (1, 2, 1, '2022-12-02');
INSERT INTO `detallegalpon_cerdo` VALUES (2, 2, 2, '2022-12-02');
INSERT INTO `detallegalpon_cerdo` VALUES (3, 3, 3, '2022-12-02');
INSERT INTO `detallegalpon_cerdo` VALUES (4, 3, 4, '2022-12-02');
INSERT INTO `detallegalpon_cerdo` VALUES (5, 4, 5, '2022-12-14');

-- ----------------------------
-- Table structure for empresa
-- ----------------------------
DROP TABLE IF EXISTS `empresa`;
CREATE TABLE `empresa`  (
  `id_hacienda` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `ruc` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `correo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `encargado` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `direccion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_hacienda`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of empresa
-- ----------------------------
INSERT INTO `empresa` VALUES (1, 'Nombre de hacienda', '0985906677', '0940321854', 'elgamer-26@hotmail.com', '20230102135754pigs1.jpg', 'Encargado', 'Descripción de hacienda', 'Dirección');

-- ----------------------------
-- Table structure for enfermedad
-- ----------------------------
DROP TABLE IF EXISTS `enfermedad`;
CREATE TABLE `enfermedad`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of enfermedad
-- ----------------------------
INSERT INTO `enfermedad` VALUES (1, 'RABIA editada', 'RABIA ES editada', 1);
INSERT INTO `enfermedad` VALUES (2, 'cerdo loko', 'cerdo con rabia ', 1);

-- ----------------------------
-- Table structure for enfermedad_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `enfermedad_cerdo`;
CREATE TABLE `enfermedad_cerdo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `cerdo_id` int NULL DEFAULT NULL,
  `veterinario_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `sintomas` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `diagnostico` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cerdo_id`(`cerdo_id`) USING BTREE,
  INDEX `veterinario_id`(`veterinario_id`) USING BTREE,
  CONSTRAINT `enfermedad_cerdo_ibfk_1` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `enfermedad_cerdo_ibfk_2` FOREIGN KEY (`veterinario_id`) REFERENCES `veterinario` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of enfermedad_cerdo
-- ----------------------------
INSERT INTO `enfermedad_cerdo` VALUES (5, 1, 2, '2022-10-08', 'Sintomas', 'Diagnóstico', 0);
INSERT INTO `enfermedad_cerdo` VALUES (6, 2, 1, '2022-10-12', 'Sintomas', 'Diagnóstico', 0);
INSERT INTO `enfermedad_cerdo` VALUES (7, 1, 2, '2022-10-12', 'AAAAAAA', 'BBBBBBB', 0);
INSERT INTO `enfermedad_cerdo` VALUES (8, 3, 2, '2022-12-13', 'OJOS ROJOS, VÓMITO', 'TIENE PARASITOS', 0);
INSERT INTO `enfermedad_cerdo` VALUES (11, 1, 1, '2022-12-13', 'AA', 'AAA', 1);
INSERT INTO `enfermedad_cerdo` VALUES (12, 2, 1, '2022-12-13', 'aaaaaaa', 'bbbbb', 1);

-- ----------------------------
-- Table structure for galpon
-- ----------------------------
DROP TABLE IF EXISTS `galpon`;
CREATE TABLE `galpon`  (
  `id_galpon` int NOT NULL AUTO_INCREMENT,
  `numero` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `id_tipo` int NULL DEFAULT NULL,
  `capacidad` int NULL DEFAULT NULL,
  `observacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `disponible` int NULL DEFAULT 1,
  PRIMARY KEY (`id_galpon`) USING BTREE,
  INDEX `id_tipo`(`id_tipo`) USING BTREE,
  CONSTRAINT `galpon_ibfk_1` FOREIGN KEY (`id_tipo`) REFERENCES `tipo_galpon` (`id_tipo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of galpon
-- ----------------------------
INSERT INTO `galpon` VALUES (1, '123', 2, 3, 'para criar chancho', 1, 0);
INSERT INTO `galpon` VALUES (2, '321', 1, 5, 'aaa', 1, 0);
INSERT INTO `galpon` VALUES (3, '66789', 2, 20, 'PARA LOS CERDO BERRACOS', 1, 1);
INSERT INTO `galpon` VALUES (4, '13265', 5, 15, 'GALPÓN PARA TRASPASO DE CERDOS', 1, 0);
INSERT INTO `galpon` VALUES (5, '13544', 3, 5, 'PARA LAS CERDAS EN CELO', 1, 1);

-- ----------------------------
-- Table structure for galpon_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `galpon_cerdo`;
CREATE TABLE `galpon_cerdo`  (
  `id_galpon_cerdo` int NOT NULL AUTO_INCREMENT,
  `id_galpon` int NULL DEFAULT NULL,
  `id_cerdo` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id_galpon_cerdo`) USING BTREE,
  INDEX `id_galpon`(`id_galpon`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `galpon_cerdo_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpon` (`id_galpon`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `galpon_cerdo_ibfk_2` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of galpon_cerdo
-- ----------------------------

-- ----------------------------
-- Table structure for galpon_cerdo_new
-- ----------------------------
DROP TABLE IF EXISTS `galpon_cerdo_new`;
CREATE TABLE `galpon_cerdo_new`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_galpon` int NULL DEFAULT NULL,
  `fecha_i` date NULL DEFAULT NULL,
  `fecha_f` date NULL DEFAULT NULL,
  `semana` int NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_galpon`(`id_galpon`) USING BTREE,
  CONSTRAINT `galpon_cerdo_new_ibfk_1` FOREIGN KEY (`id_galpon`) REFERENCES `galpon` (`id_galpon`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of galpon_cerdo_new
-- ----------------------------
INSERT INTO `galpon_cerdo_new` VALUES (2, 1, '2022-12-02', '2023-05-11', 23, 1);
INSERT INTO `galpon_cerdo_new` VALUES (3, 2, '2022-12-02', '2023-04-23', 20, 1);
INSERT INTO `galpon_cerdo_new` VALUES (4, 4, '2022-12-14', '2023-05-01', 20, 1);

-- ----------------------------
-- Table structure for insumo
-- ----------------------------
DROP TABLE IF EXISTS `insumo`;
CREATE TABLE `insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `presentacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  CONSTRAINT `insumo_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of insumo
-- ----------------------------
INSERT INTO `insumo` VALUES (1, '92512111', 'Insumo cerdo', 1, 37, 30.25, ' Detalle del medicamento editado', 'insumo.jpg', 1, 'Presentación 2x3');
INSERT INTO `insumo` VALUES (2, '399055551', 'Nombre del insumo', 3, 39, 12.00, ' Detalle del insumo', 'insumo.jpg', 1, 'Presentación 200b');
INSERT INTO `insumo` VALUES (3, '4455', 'Insumo de limpieza', 4, 1, 5.00, ' detalle del insumo', 'insumo.jpg', 1, 'limpieza 100x100');

-- ----------------------------
-- Table structure for lote_alimento
-- ----------------------------
DROP TABLE IF EXISTS `lote_alimento`;
CREATE TABLE `lote_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `alimento_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `fecha_i` date NULL DEFAULT NULL,
  `fecha_f` date NULL DEFAULT NULL,
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `alimento_id`(`alimento_id`) USING BTREE,
  CONSTRAINT `lote_alimento_ibfk_1` FOREIGN KEY (`alimento_id`) REFERENCES `alimento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lote_alimento
-- ----------------------------
INSERT INTO `lote_alimento` VALUES (6, 1, 38, '2022-12-04', '2022-12-04', 'CAL-7645', '2022-12-04 08:53:12');
INSERT INTO `lote_alimento` VALUES (8, 1, 300, '2022-12-04', '2023-01-05', 'CAL-9108', '2022-12-04 08:56:16');
INSERT INTO `lote_alimento` VALUES (9, 2, 1477, '2022-12-04', '2026-10-14', 'CAL-4219', '2022-12-04 08:56:16');
INSERT INTO `lote_alimento` VALUES (10, 3, 2380, '2022-12-04', '2023-10-11', 'CAL-6271', '2022-12-04 08:56:16');
INSERT INTO `lote_alimento` VALUES (12, 5, 6000, '2022-12-04', '2024-06-05', 'CAL-2381', '2022-12-04 08:56:16');

-- ----------------------------
-- Table structure for lote_insumo
-- ----------------------------
DROP TABLE IF EXISTS `lote_insumo`;
CREATE TABLE `lote_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `insumo_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `fecha_i` date NULL DEFAULT NULL,
  `fecha_f` date NULL DEFAULT NULL,
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `insumo_id`(`insumo_id`) USING BTREE,
  CONSTRAINT `lote_insumo_ibfk_1` FOREIGN KEY (`insumo_id`) REFERENCES `insumo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lote_insumo
-- ----------------------------
INSERT INTO `lote_insumo` VALUES (2, 1, 30, '2022-12-10', '2023-10-31', 'CIL-5147', '2022-12-10 13:45:07');
INSERT INTO `lote_insumo` VALUES (3, 1, 9, '2021-10-13', '2024-11-06', 'CIL-1818', '2022-12-13 09:55:00');
INSERT INTO `lote_insumo` VALUES (4, 2, 9, '2022-07-12', '2023-11-30', 'CIL-5093', '2022-12-13 09:55:00');

-- ----------------------------
-- Table structure for lote_medicamento
-- ----------------------------
DROP TABLE IF EXISTS `lote_medicamento`;
CREATE TABLE `lote_medicamento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `medicamento_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `fecha_i` date NULL DEFAULT NULL,
  `fecha_f` date NULL DEFAULT NULL,
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `medicamento_id`(`medicamento_id`) USING BTREE,
  CONSTRAINT `lote_medicamento_ibfk_1` FOREIGN KEY (`medicamento_id`) REFERENCES `medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lote_medicamento
-- ----------------------------
INSERT INTO `lote_medicamento` VALUES (2, 4, 26, '2022-12-08', '2022-12-08', 'CML-2698', '2022-12-08 13:06:30');
INSERT INTO `lote_medicamento` VALUES (4, 6, 46, '2022-05-01', '2024-02-20', 'CML-1496', '2022-12-12 15:22:32');

-- ----------------------------
-- Table structure for lote_vacuna
-- ----------------------------
DROP TABLE IF EXISTS `lote_vacuna`;
CREATE TABLE `lote_vacuna`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `vacuna_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `fecha_i` date NULL DEFAULT NULL,
  `fecha_f` date NULL DEFAULT NULL,
  `codigo` char(40) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `vacuna_id`(`vacuna_id`) USING BTREE,
  CONSTRAINT `lote_vacuna_ibfk_1` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lote_vacuna
-- ----------------------------
INSERT INTO `lote_vacuna` VALUES (3, 1, 445, '2022-12-03', '2024-01-30', 'CVL-3635', '2022-12-03 16:14:33');
INSERT INTO `lote_vacuna` VALUES (4, 2, 30, '2022-12-03', '2023-12-29', 'CVL-5293', '2022-12-03 16:14:33');
INSERT INTO `lote_vacuna` VALUES (5, 3, 60, '2022-12-03', '2024-03-06', 'CVL-1129', '2022-12-03 16:14:33');
INSERT INTO `lote_vacuna` VALUES (6, 1, 400, '2022-12-03', '2025-11-13', 'CVL-4117', '2022-12-03 18:14:11');
INSERT INTO `lote_vacuna` VALUES (7, 2, 50, '2022-12-03', '2024-10-23', 'CVL-6653', '2022-12-03 18:14:11');
INSERT INTO `lote_vacuna` VALUES (8, 3, 90, '2022-12-03', '2028-06-07', 'CVL-8927', '2022-12-03 18:14:11');
INSERT INTO `lote_vacuna` VALUES (9, 4, 123, '2022-12-03', '2024-10-16', 'CVL-3643', '2022-12-03 18:14:11');
INSERT INTO `lote_vacuna` VALUES (10, 5, 321, '2022-12-03', '2025-06-04', 'CVL-5115', '2022-12-03 18:14:11');
INSERT INTO `lote_vacuna` VALUES (12, 2, 80, '2022-12-04', '2022-12-04', 'CVL-6563', '2022-12-04 09:13:39');

-- ----------------------------
-- Table structure for marca_alimento
-- ----------------------------
DROP TABLE IF EXISTS `marca_alimento`;
CREATE TABLE `marca_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `marca_alimento` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of marca_alimento
-- ----------------------------
INSERT INTO `marca_alimento` VALUES (1, 'LOS 3 CHANCHITOS', 1);
INSERT INTO `marca_alimento` VALUES (2, 'EL CERDON', 1);
INSERT INTO `marca_alimento` VALUES (3, 'PORKY PIG', 1);
INSERT INTO `marca_alimento` VALUES (4, 'CONEJO', 1);
INSERT INTO `marca_alimento` VALUES (5, 'EL MACHON', 1);

-- ----------------------------
-- Table structure for medicamento
-- ----------------------------
DROP TABLE IF EXISTS `medicamento`;
CREATE TABLE `medicamento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT 0,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `presentacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `unidades` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  CONSTRAINT `medicamento_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_medicamento` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of medicamento
-- ----------------------------
INSERT INTO `medicamento` VALUES (4, '577707426', 'Biomacrotil Premix', 1, 53, 12.00, ' Detalle del medicamento', 'medicamento.jpg', 1, 'Cali-Dex 200.', 7);
INSERT INTO `medicamento` VALUES (5, '141777745', 'Biomacrotil PS.', 2, 10, 20.75, ' Medicamento para el cerdo enfermo', 'medicamento.jpg', 1, 'Cali-Dex 200.', 7);
INSERT INTO `medicamento` VALUES (6, '24568', 'Biomacrotil 200.', 1, 1, 10.00, 'Medicamento para el cerdo de tipo pastilla ingreso via oral', 'medicamento.jpg', 1, 'Cali-Dex 200.', 5);

-- ----------------------------
-- Table structure for movimientos
-- ----------------------------
DROP TABLE IF EXISTS `movimientos`;
CREATE TABLE `movimientos`  (
  `id_m` int NOT NULL AUTO_INCREMENT,
  `id_g_c` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `hasta` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id_m`) USING BTREE,
  INDEX `id_g_c`(`id_g_c`) USING BTREE,
  CONSTRAINT `movimientos_ibfk_1` FOREIGN KEY (`id_g_c`) REFERENCES `galpon_cerdo` (`id_galpon_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of movimientos
-- ----------------------------

-- ----------------------------
-- Table structure for muertes
-- ----------------------------
DROP TABLE IF EXISTS `muertes`;
CREATE TABLE `muertes`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cerdo` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `motivo` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `id_galpon` int NULL DEFAULT 1,
  `hora` time(0) NULL DEFAULT NULL,
  `semana` int NULL DEFAULT NULL,
  `f_registro` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `id_cerdo`(`id_cerdo`) USING BTREE,
  CONSTRAINT `muertes_ibfk_1` FOREIGN KEY (`id_cerdo`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of muertes
-- ----------------------------
INSERT INTO `muertes` VALUES (7, 1, '2022-12-14', 'POR ENFERMEDAD PORCINA DEL CERDO', 2, '10:53:00', 3, '2022-12-14 08:52:28');

-- ----------------------------
-- Table structure for pedidos_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `pedidos_cerdo`;
CREATE TABLE `pedidos_cerdo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_pedido` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `apellido` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `cedula` char(13) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `correo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `direccion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 2,
  `iva` int NULL DEFAULT 12,
  `fecha_pedido` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pedidos_cerdo
-- ----------------------------
INSERT INTO `pedidos_cerdo` VALUES (6, '49476732', 'JOSE ', 'VILACRES', '123456789', '0940321854', 'ELGAMER-26@HOTMAIL.COM', 'MILAGRO', 600.00, 72.00, 672.00, 1, 12, '2023-01-06 09:29:13');
INSERT INTO `pedidos_cerdo` VALUES (7, '96229837', 'JORGE', 'WONG', '0987654321', '0940321854', 'ELGAMER-26@HOTMAIL.COM', 'DURAN, LA ALBORADA', 375.00, 45.00, 420.00, 1, 12, '2023-01-06 11:16:09');
INSERT INTO `pedidos_cerdo` VALUES (8, '30215611', 'JORGE', 'WONG', '0987654321', '0940321854', 'ELGAMER-26@HOTMAIL.COM', 'DURAN, LA ALBORADA', 375.00, 45.00, 420.00, 1, 12, '2023-01-06 11:16:14');
INSERT INTO `pedidos_cerdo` VALUES (9, '33519339', 'JOSE ', 'RAMOS', '0940321854', '0940321854', 'ELGAMER-26@HOTMAIL.COM', 'MILAGRO', 260.00, 31.20, 291.20, 2, 12, '2023-01-06 11:22:11');
INSERT INTO `pedidos_cerdo` VALUES (10, '71583371', 'JOSE MARIA', 'VALASCO IBARRA', '1234567890', '0940321854', 'elgamer-26@hotmai.com', 'milagro uae', 160.00, 19.20, 179.20, 0, 12, '2023-01-06 20:55:35');
INSERT INTO `pedidos_cerdo` VALUES (11, '69965493', 'MILTON EDUARDO', 'OCHOA NOCANCELA', '1234567890', '0940321854', 'elgamer-26@hotmail.com', 'MI CASA', 475.00, 57.00, 532.00, 0, 12, '2023-01-06 21:01:14');

-- ----------------------------
-- Table structure for permisos
-- ----------------------------
DROP TABLE IF EXISTS `permisos`;
CREATE TABLE `permisos`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `rol_id` int NULL DEFAULT NULL,
  `usuario` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `config` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `cerdo` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `galpon` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `compra_venta` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `alimentacion` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `vacuna_despara` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `enfermedad_tratamiento` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `informes` char(10) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `rol_id`(`rol_id`) USING BTREE,
  CONSTRAINT `permisos_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`rol_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of permisos
-- ----------------------------
INSERT INTO `permisos` VALUES (2, 10, 'false', 'false', 'true', 'true', 'false', 'false', 'false', 'false', 'false');
INSERT INTO `permisos` VALUES (3, 1, 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true', 'true');
INSERT INTO `permisos` VALUES (4, 11, 'false', 'false', 'false', 'false', 'true', 'false', 'false', 'false', 'true');

-- ----------------------------
-- Table structure for peso_cerdo
-- ----------------------------
DROP TABLE IF EXISTS `peso_cerdo`;
CREATE TABLE `peso_cerdo`  (
  `peso_id` int NOT NULL AUTO_INCREMENT,
  `cerdo_id` int NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  `metodo` char(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `peso_pasado` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nuevo_pesaje` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `etapa_fase` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `perimetro_t` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `largo_c` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `observacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `semana` int NULL DEFAULT NULL,
  PRIMARY KEY (`peso_id`) USING BTREE,
  INDEX `cerdo_id`(`cerdo_id`) USING BTREE,
  CONSTRAINT `peso_cerdo_ibfk_1` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of peso_cerdo
-- ----------------------------
INSERT INTO `peso_cerdo` VALUES (10, 3, '2022-12-03 09:59:47', 'exacto', '80', '25', 'Iniciador', '', '', 'Observación el peso de cerdo', 1, 1);
INSERT INTO `peso_cerdo` VALUES (11, 4, '2022-12-03 10:57:21', 'exacto', '90', '45', 'Crecimiento', '', '', 'ya esta agrande', 1, 1);
INSERT INTO `peso_cerdo` VALUES (12, 2, '2022-12-03 10:57:38', 'exacto', '20', '25', 'Iniciador', '', '', 'esta grande', 1, 1);
INSERT INTO `peso_cerdo` VALUES (13, 3, '2022-12-03 11:09:42', 'exacto', '25', '56', 'Desarrollo', '', '', 'Observación', 1, 1);
INSERT INTO `peso_cerdo` VALUES (14, 1, '2022-12-03 11:12:39', 'exacto', '50', '23', 'Iniciador', '', '', 'aaaaaaaa', 1, 1);
INSERT INTO `peso_cerdo` VALUES (15, 1, '2022-12-03 11:15:17', 'exacto', '23', '30', 'Iniciador', '', '', 'bbbb', 1, 1);
INSERT INTO `peso_cerdo` VALUES (16, 3, '2022-12-04 11:43:48', 'exacto', '56', '30', 'Iniciador', '', '', 'pesaje del cerdo', 1, 1);
INSERT INTO `peso_cerdo` VALUES (17, 3, '2022-12-04 18:17:49', 'vivo', '30', '44', 'Crecimiento', '90', '80', 'Cerdo mas gordo y grande', 1, 1);
INSERT INTO `peso_cerdo` VALUES (18, 3, '2022-12-13 12:20:05', 'exacto', '44', '50', 'Crecimiento', '', '', 'EN CRECIMIENTO', 1, 3);
INSERT INTO `peso_cerdo` VALUES (19, 5, '2022-12-14 12:22:27', 'exacto', '5', '6', '', '', '', 'PESO DEL CERDO', 1, 1);
INSERT INTO `peso_cerdo` VALUES (20, 5, '2022-12-14 17:09:36', 'exacto', '6', '7', 'Preiniciador', '', '', 'mas pesada', 1, 1);

-- ----------------------------
-- Table structure for proveedor
-- ----------------------------
DROP TABLE IF EXISTS `proveedor`;
CREATE TABLE `proveedor`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `razon` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `ruc` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `correo` varchar(150) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `encargado` varchar(200) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono_en` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `direccion` varchar(150) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of proveedor
-- ----------------------------
INSERT INTO `proveedor` VALUES (1, 'LA GRANJA', '0940321854001', '0987654321', 'elgamer@hotmail.com', ' LA MEJOR CALIDAD DE COMIDA Y DE CERDO', 'YO MISMO', '54321', 'milagro ', 1);

-- ----------------------------
-- Table structure for raza
-- ----------------------------
DROP TABLE IF EXISTS `raza`;
CREATE TABLE `raza`  (
  `id_raza` int NOT NULL AUTO_INCREMENT,
  `raza` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id_raza`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of raza
-- ----------------------------
INSERT INTO `raza` VALUES (1, 'PORKY', 1);
INSERT INTO `raza` VALUES (2, 'PIETRAIN', 1);
INSERT INTO `raza` VALUES (3, 'HAMPSHIRE', 1);
INSERT INTO `raza` VALUES (4, 'LARGE WHITE', 1);
INSERT INTO `raza` VALUES (5, 'LANDRACE', 1);
INSERT INTO `raza` VALUES (6, 'YORKSHIRE', 1);
INSERT INTO `raza` VALUES (7, 'ROSSE', 1);

-- ----------------------------
-- Table structure for rol
-- ----------------------------
DROP TABLE IF EXISTS `rol`;
CREATE TABLE `rol`  (
  `rol_id` int NOT NULL AUTO_INCREMENT,
  `rol` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`rol_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 14 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rol
-- ----------------------------
INSERT INTO `rol` VALUES (1, 'Administrador', 1);
INSERT INTO `rol` VALUES (10, 'Alimentador', 1);
INSERT INTO `rol` VALUES (11, 'Vendedor', 1);

-- ----------------------------
-- Table structure for tipo_alimentcion
-- ----------------------------
DROP TABLE IF EXISTS `tipo_alimentcion`;
CREATE TABLE `tipo_alimentcion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_alimentcion
-- ----------------------------
INSERT INTO `tipo_alimentcion` VALUES (1, 'engorda', 1);
INSERT INTO `tipo_alimentcion` VALUES (2, 'crecimiento', 1);

-- ----------------------------
-- Table structure for tipo_alimento
-- ----------------------------
DROP TABLE IF EXISTS `tipo_alimento`;
CREATE TABLE `tipo_alimento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_alimento` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_alimento
-- ----------------------------
INSERT INTO `tipo_alimento` VALUES (1, 'ENGORDA', 1);
INSERT INTO `tipo_alimento` VALUES (2, 'SALUD', 1);
INSERT INTO `tipo_alimento` VALUES (3, 'ESTADO FISICO', 1);
INSERT INTO `tipo_alimento` VALUES (4, 'PROCREACION', 1);
INSERT INTO `tipo_alimento` VALUES (5, 'FITNESS', 1);

-- ----------------------------
-- Table structure for tipo_galpon
-- ----------------------------
DROP TABLE IF EXISTS `tipo_galpon`;
CREATE TABLE `tipo_galpon`  (
  `id_tipo` int NOT NULL AUTO_INCREMENT,
  `tipo_galpon` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id_tipo`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_galpon
-- ----------------------------
INSERT INTO `tipo_galpon` VALUES (1, 'GOLPON LECHON', 1);
INSERT INTO `tipo_galpon` VALUES (2, 'GALPON BERRACO', 1);
INSERT INTO `tipo_galpon` VALUES (3, 'GALPON DE HEMBRAS EN CELO', 1);
INSERT INTO `tipo_galpon` VALUES (4, 'GALPON DE MACHOS EN CELO', 1);
INSERT INTO `tipo_galpon` VALUES (5, 'GALPÓN TRASPASO', 1);

-- ----------------------------
-- Table structure for tipo_insumo
-- ----------------------------
DROP TABLE IF EXISTS `tipo_insumo`;
CREATE TABLE `tipo_insumo`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_insumo
-- ----------------------------
INSERT INTO `tipo_insumo` VALUES (1, 'ALCOOHOL', 1);
INSERT INTO `tipo_insumo` VALUES (2, 'TIJERAS', 1);
INSERT INTO `tipo_insumo` VALUES (3, 'JERINGAS', 1);
INSERT INTO `tipo_insumo` VALUES (4, 'ALGODÓN', 1);

-- ----------------------------
-- Table structure for tipo_medicamento
-- ----------------------------
DROP TABLE IF EXISTS `tipo_medicamento`;
CREATE TABLE `tipo_medicamento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_medicamento
-- ----------------------------
INSERT INTO `tipo_medicamento` VALUES (1, 'PASTILLAS', 1);
INSERT INTO `tipo_medicamento` VALUES (2, 'SUERO', 1);
INSERT INTO `tipo_medicamento` VALUES (3, 'FARMACOS', 1);

-- ----------------------------
-- Table structure for tipo_tratamiento
-- ----------------------------
DROP TABLE IF EXISTS `tipo_tratamiento`;
CREATE TABLE `tipo_tratamiento`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `descripcion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_tratamiento
-- ----------------------------
INSERT INTO `tipo_tratamiento` VALUES (1, 'Tipo tratamiento', 'Descripción', 1);
INSERT INTO `tipo_tratamiento` VALUES (2, ' editado', ' Descripción editado', 1);

-- ----------------------------
-- Table structure for tipo_vacuna
-- ----------------------------
DROP TABLE IF EXISTS `tipo_vacuna`;
CREATE TABLE `tipo_vacuna`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_vacuna` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tipo_vacuna
-- ----------------------------
INSERT INTO `tipo_vacuna` VALUES (1, 'Rinitis atrófica', 1);
INSERT INTO `tipo_vacuna` VALUES (2, 'Rinitis', 1);
INSERT INTO `tipo_vacuna` VALUES (3, 'Parvovirus', 1);

-- ----------------------------
-- Table structure for tratamiento_cerdos
-- ----------------------------
DROP TABLE IF EXISTS `tratamiento_cerdos`;
CREATE TABLE `tratamiento_cerdos`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `enfer_cerdo_id` int NULL DEFAULT NULL,
  `peso` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `fecha_i` date NULL DEFAULT NULL,
  `fecha_f` date NULL DEFAULT NULL,
  `observacion` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `estado` int NULL DEFAULT 1,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0) ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `enfer_cerdo_id`(`enfer_cerdo_id`) USING BTREE,
  CONSTRAINT `tratamiento_cerdos_ibfk_1` FOREIGN KEY (`enfer_cerdo_id`) REFERENCES `enfermedad_cerdo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of tratamiento_cerdos
-- ----------------------------
INSERT INTO `tratamiento_cerdos` VALUES (16, 5, '123 Kg', '2022-10-12', '2022-10-12', 'Observación', 1, '2022-10-12 14:06:31');
INSERT INTO `tratamiento_cerdos` VALUES (17, 6, '110 Kg', '2022-10-12', '2022-10-12', 'Observación', 1, '2022-10-12 14:51:00');
INSERT INTO `tratamiento_cerdos` VALUES (18, 7, '123 Kg', '2022-10-12', '2022-10-12', '1234567890 DE TODO UN POCO', 1, '2022-10-12 14:52:49');
INSERT INTO `tratamiento_cerdos` VALUES (19, 8, '44 Kg', '2022-06-13', '2023-07-05', 'para salvar a cerdo se lo tratará con medicamentos', 1, '2022-12-13 10:30:18');

-- ----------------------------
-- Table structure for usuario
-- ----------------------------
DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario`  (
  `usuario_id` int NOT NULL AUTO_INCREMENT,
  `nombres` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `apellidos` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `usuario` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `passwordd` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `rol_id` int NULL DEFAULT NULL,
  `domicilio` varchar(200) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` varchar(200) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `correo` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `cedula` char(11) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`usuario_id`) USING BTREE,
  INDEX `rol_id`(`rol_id`) USING BTREE,
  CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`rol_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 19 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usuario
-- ----------------------------
INSERT INTO `usuario` VALUES (1, 'PORKY', 'CERDO', 'admin', '123', 1, 'casa', '123', 'user.png', 1, 'elgamer-26@hotmail.com', '1234567891');
INSERT INTO `usuario` VALUES (9, 'JOSEE', 'VILLACRES', 'asa', 'Jorge2´+', 1, 'asa', 'asas', 'user.png', 1, '2elgamer-26@hotmail.com', '1234567892');
INSERT INTO `usuario` VALUES (11, 'JORGE', 'WONG', 'Jorge', 'Jorge12q,.', 1, 'MILAGRO', '0987654321', 'user.png', 1, '3elgamer-26@hotmail.com', '1234567893');
INSERT INTO `usuario` VALUES (13, 'LA ROSALIA', 'ROSA', 'AdminInsetech', 'W2K8eZ-iuRY/', 10, 'MILAGRO ', '0940321854', 'user.png', 1, 'Telgamer-26@hotmail.com', '1234567894');
INSERT INTO `usuario` VALUES (17, 'DANIEL ', 'FLORES', 'Lokochon', 'Ooi6XcR8DWlb', 10, 'NARANJITO', '6789012345', 'user.png', 1, 'detodo@hotmail.com', '0940321854');
INSERT INTO `usuario` VALUES (18, 'ALBERT', 'WESKER', 'mapache', 'Voc-m&B45CJM', 11, 'RACCONN CITY', '0987654321', 'user.png', 1, 'computacioneinformaticauae@gmail.com', '0941129603');

-- ----------------------------
-- Table structure for vacuna
-- ----------------------------
DROP TABLE IF EXISTS `vacuna`;
CREATE TABLE `vacuna`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `codigo` char(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `tipo_id` int NULL DEFAULT NULL,
  `cantidad` int NULL DEFAULT NULL,
  `precio` decimal(10, 2) NULL DEFAULT NULL,
  `detalle` text CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL,
  `presentacion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  `registro_sani` varchar(150) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `cantidad_dosis` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `tipo_id`(`tipo_id`) USING BTREE,
  CONSTRAINT `vacuna_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipo_vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of vacuna
-- ----------------------------
INSERT INTO `vacuna` VALUES (1, '353287080', 'Nombre editado', 1, 1122, 10.00, ' Detalle de la vacuna del cerdo editado', 'Presentación editado', 'vacuna.jpg', 1, 'ASDV543', 40);
INSERT INTO `vacuna` VALUES (2, '999271877', 'Nombre de la vacuna', 2, 181, 100.00, ' Detalle de la vacuna del cerdo para los cerdos', 'Presentación 10x100 de todo', 'vacuna.jpg', 1, 'ASDV543', 40);
INSERT INTO `vacuna` VALUES (3, '985531120', 'PORCINITIS', 3, 151, 100.00, ' TOMAR SOLO SI ES UN CERDO NO PARA HUMANOS', 'PASTILLAS PARA EL DOLOR DE CABEZA DEL CERDOS DE 100ML', 'vacuna.jpg', 1, 'ASDV543', 40);
INSERT INTO `vacuna` VALUES (4, '5538', 'BLUE GLASS EDIT', 3, 124, 70.00, ' Detalle de la vacuna del cerdo', 'BLUE GLASS EDIT400', 'vacuna.jpg', 1, 'ASDV543', 40);
INSERT INTO `vacuna` VALUES (5, '58208', 'BLUE GLASS LOL', 3, 322, 20.00, ' Detalle de la vacuna del cerdo', 'Presentación', 'vacuna.jpg', 1, 'Registro sanitario b', 20);

-- ----------------------------
-- Table structure for vacunacion
-- ----------------------------
DROP TABLE IF EXISTS `vacunacion`;
CREATE TABLE `vacunacion`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `cerdo_id` int NULL DEFAULT NULL,
  `vacuna_id` int NULL DEFAULT NULL,
  `semana` int NULL DEFAULT NULL,
  `dosis` int NULL DEFAULT NULL,
  `fecha` timestamp(0) NULL DEFAULT CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cerdo_id`(`cerdo_id`) USING BTREE,
  INDEX `vacuna_id`(`vacuna_id`) USING BTREE,
  CONSTRAINT `vacunacion_ibfk_1` FOREIGN KEY (`cerdo_id`) REFERENCES `cerdo` (`id_cerdo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `vacunacion_ibfk_2` FOREIGN KEY (`vacuna_id`) REFERENCES `vacuna` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of vacunacion
-- ----------------------------
INSERT INTO `vacunacion` VALUES (7, 3, 1, 1, 10, '2022-12-04 13:25:23');
INSERT INTO `vacunacion` VALUES (8, 3, 1, 1, 20, '2022-12-04 13:28:35');
INSERT INTO `vacunacion` VALUES (9, 4, 1, 1, 20, '2022-12-04 13:41:16');
INSERT INTO `vacunacion` VALUES (10, 4, 1, 1, 40, '2022-12-04 13:41:32');
INSERT INTO `vacunacion` VALUES (11, 1, 1, 1, 10, '2022-12-04 13:42:39');
INSERT INTO `vacunacion` VALUES (12, 2, 1, 1, 100, '2022-12-04 13:43:15');
INSERT INTO `vacunacion` VALUES (13, 3, 1, 1, 20, '2022-12-04 19:24:55');
INSERT INTO `vacunacion` VALUES (14, 4, 1, 1, 20, '2022-12-04 19:24:55');
INSERT INTO `vacunacion` VALUES (15, 1, 1, 1, 5, '2022-12-04 19:28:13');
INSERT INTO `vacunacion` VALUES (16, 2, 1, 1, 5, '2022-12-04 19:28:13');
INSERT INTO `vacunacion` VALUES (17, 3, 1, 1, 2, '2022-12-04 19:51:47');
INSERT INTO `vacunacion` VALUES (18, 5, 1, 1, 2, '2022-12-14 12:22:06');
INSERT INTO `vacunacion` VALUES (19, 5, 1, 1, 2, '2022-12-14 20:08:46');
INSERT INTO `vacunacion` VALUES (20, 3, 1, 3, 2, '2022-12-15 18:46:15');
INSERT INTO `vacunacion` VALUES (21, 4, 1, 3, 2, '2022-12-15 18:46:15');
INSERT INTO `vacunacion` VALUES (22, 3, 1, 3, 2, '2022-12-15 18:48:53');
INSERT INTO `vacunacion` VALUES (23, 4, 1, 3, 2, '2022-12-15 18:48:53');
INSERT INTO `vacunacion` VALUES (24, 5, 1, 1, 1, '2022-12-15 18:49:48');

-- ----------------------------
-- Table structure for venta_cerdos
-- ----------------------------
DROP TABLE IF EXISTS `venta_cerdos`;
CREATE TABLE `venta_cerdos`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NULL DEFAULT NULL,
  `fecha` date NULL DEFAULT NULL,
  `numero_venta` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(50) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `iva` int NULL DEFAULT NULL,
  `subtotal` decimal(10, 2) NULL DEFAULT NULL,
  `impuesto` decimal(10, 2) NULL DEFAULT NULL,
  `total` decimal(10, 2) NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `cliente_id`(`cliente_id`) USING BTREE,
  CONSTRAINT `venta_cerdos_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of venta_cerdos
-- ----------------------------
INSERT INTO `venta_cerdos` VALUES (3, 1, '2022-12-15', '123456532', 'Factura', 12, 125.00, 15.00, 140.00, 1);
INSERT INTO `venta_cerdos` VALUES (4, 2, '2023-01-02', '0912121212', 'Factura', 12, 5815.00, 697.80, 6512.80, 1);
INSERT INTO `venta_cerdos` VALUES (5, 2, '2023-01-02', '1212133', 'Factura', 12, 11700.00, 1404.00, 13104.00, 1);

-- ----------------------------
-- Table structure for veterinario
-- ----------------------------
DROP TABLE IF EXISTS `veterinario`;
CREATE TABLE `veterinario`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `apellido` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `documento` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `telefono` char(15) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `direccion` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `sucursal` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `estado` int NULL DEFAULT 1,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of veterinario
-- ----------------------------
INSERT INTO `veterinario` VALUES (1, 'Nombres', 'Apelllidos editado', '0940321855', '1234567890', 'Naranjito editado', 'SUPER CAT editado', 1);
INSERT INTO `veterinario` VALUES (2, 'BACILIO TONTO', 'AAAAAA BBBBBB', '0940321854', '0985906677', 'milagro', 'VANESUR', 1);

-- ----------------------------
-- Table structure for web
-- ----------------------------
DROP TABLE IF EXISTS `web`;
CREATE TABLE `web`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `foto1` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto2` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `foto3` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `detalle1` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `detalle2` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  `detalle3` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_spanish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web
-- ----------------------------
INSERT INTO `web` VALUES (1, '202301021358261434829025827.jpg', '20230102140509118159693_4384045835002731_5782836742516971640_n.jpg', '20230102135821pigs1.jpg', 'Los mejores cerdos', 'La  mejor calidad de cerdo', 'Los cerdos son cerdos y ricos ');

-- ----------------------------
-- Procedure structure for costro_produccion_cerdo
-- ----------------------------
DROP PROCEDURE IF EXISTS `costro_produccion_cerdo`;
delimiter ;;
CREATE PROCEDURE `costro_produccion_cerdo`(in ind int)
BEGIN

DECLARE alimento DECIMAL(10,2);
DECLARE vacuna DECIMAL(10,2);
DECLARE desparasitante DECIMAL(10,2);
DECLARE insumo DECIMAL(10,2);
DECLARE medicamento DECIMAL(10,2);

SELECT 
ROUND( SUM(( alimento.precio / alimento.peso ) * alimentacion.cantidad ), 2)  INTO alimento
FROM
	alimentacion
	INNER JOIN alimento ON alimentacion.alimento_id = alimento.id 
WHERE
	alimentacion.id_cerdo = ind 
GROUP BY
	alimentacion.id_cerdo; 
	
SELECT 
ROUND( SUM(( vacuna.precio / vacuna.cantidad_dosis ) * vacunacion.dosis ), 2 ) INTO vacuna
FROM
	vacunacion
	INNER JOIN vacuna ON vacunacion.vacuna_id = vacuna.id 
WHERE
	vacunacion.cerdo_id = ind 
GROUP BY
	vacunacion.cerdo_id;
	
SELECT 
ROUND( SUM(( medicamento.precio / medicamento.unidades ) * desparasitacion.cantidad ), 2) INTO desparasitante
FROM
	desparasitacion
	INNER JOIN medicamento ON desparasitacion.medicamento_id = medicamento.id 
WHERE
	desparasitacion.cerdo_id = ind 
GROUP BY
	desparasitacion.cerdo_id;
	

SELECT 
ROUND( SUM(( medicamento.precio / medicamento.unidades ) * detalle_enfermedad_medicina.cantidad ), 2) INTO medicamento
FROM
	detalle_enfermedad_medicina
	INNER JOIN tratamiento_cerdos ON detalle_enfermedad_medicina.trata_id = tratamiento_cerdos.id
	INNER JOIN enfermedad_cerdo ON tratamiento_cerdos.enfer_cerdo_id = enfermedad_cerdo.id
	INNER JOIN medicamento ON detalle_enfermedad_medicina.medicina_id = medicamento.id 
WHERE
	enfermedad_cerdo.cerdo_id = ind 
GROUP BY
	enfermedad_cerdo.cerdo_id;
	

SELECT
ROUND( SUM(( insumo.precio / detalle_enfermedad_insumo.cantidad ) * detalle_enfermedad_insumo.cantidad ), 2) INTO insumo 
FROM
	detalle_enfermedad_insumo
	INNER JOIN insumo ON detalle_enfermedad_insumo.insumo_id = insumo.id
	INNER JOIN tratamiento_cerdos ON detalle_enfermedad_insumo.tratamiento_id = tratamiento_cerdos.id
	INNER JOIN enfermedad_cerdo ON tratamiento_cerdos.enfer_cerdo_id = enfermedad_cerdo.id
	WHERE enfermedad_cerdo.cerdo_id = ind
	GROUP BY enfermedad_cerdo.cerdo_id;
	
SELECT alimento, vacuna, desparasitante, medicamento, insumo;


END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for Machoo_Hembra
-- ----------------------------
DROP PROCEDURE IF EXISTS `Machoo_Hembra`;
delimiter ;;
CREATE PROCEDURE `Machoo_Hembra`(in id int)
BEGIN

DECLARE macho int;
DECLARE hembra int;
DECLARE todo int;

SELECT
	COUNT(cerdo.sexo) as hembra INTO hembra
FROM
	detallegalpon_cerdo
	INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo WHERE cerdo.sexo = 'Hembra' AND cerdo.estado = 1 AND detallegalpon_cerdo.id_galpon = id GROUP BY 	detallegalpon_cerdo.id_galpon;
	
	SELECT
	COUNT(cerdo.sexo) as macho INTO macho
FROM
	detallegalpon_cerdo
	INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo WHERE cerdo.sexo = 'Macho' AND cerdo.estado = 1 AND detallegalpon_cerdo.id_galpon = id GROUP BY 	detallegalpon_cerdo.id_galpon;
	
		SELECT
	COUNT(cerdo.id_cerdo) as macho INTO todo
FROM
	detallegalpon_cerdo
	INNER JOIN cerdo ON detallegalpon_cerdo.id_cerdo = cerdo.id_cerdo WHERE detallegalpon_cerdo.id_galpon = id AND cerdo.estado = 1 GROUP BY detallegalpon_cerdo.id_galpon;
	
	SELECT macho, hembra, todo;

END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for sp_capacidad_disponible
-- ----------------------------
DROP PROCEDURE IF EXISTS `sp_capacidad_disponible`;
delimiter ;;
CREATE PROCEDURE `sp_capacidad_disponible`(in id int)
BEGIN
DECLARE uno int;
DECLARE dos int;

SELECT
	COUNT(id_cerdo) AS cerdos INTO uno
FROM
	galpon
	INNER JOIN galpon_cerdo ON galpon.id_galpon = galpon_cerdo.id_galpon 
WHERE
	galpon_cerdo.id_galpon = id;

SELECT capacidad INTO dos from galpon WHERE id_galpon = id;

SELECT uno, dos;

END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for sp_dasboard
-- ----------------------------
DROP PROCEDURE IF EXISTS `sp_dasboard`;
delimiter ;;
CREATE PROCEDURE `sp_dasboard`()
BEGIN
DECLARE cerdo int;
DECLARE alimento int;
DECLARE insumo int;
DECLARE medicina int;
SELECT COUNT(*) INTO cerdo FROM cerdo WHERE estado = 1 AND galpon = 'si';
SELECT COUNT(*) INTO alimento FROM alimento WHERE estado = 1;
SELECT COUNT(*) INTO insumo FROM insumo WHERE estado = 1;
SELECT COUNT(*) INTO medicina FROM medicamento WHERE estado = 1;
SELECT cerdo, alimento, insumo, medicina;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
