-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: inventory
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `username` varchar(255) DEFAULT NULL,
  `pass` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES ('Adnan Sulaiman','12345');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `base_model`
--

DROP TABLE IF EXISTS `base_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `base_model` (
  `UID` bigint NOT NULL,
  `Product_name` varchar(255) DEFAULT NULL,
  `datepurchases` date DEFAULT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `base_model`
--

LOCK TABLES `base_model` WRITE;
/*!40000 ALTER TABLE `base_model` DISABLE KEYS */;
INSERT INTO `base_model` VALUES (1001,'Keyboard',NULL),(1002,'Mouse',NULL),(1003,'Pen',NULL),(1004,'Stapler',NULL);
/*!40000 ALTER TABLE `base_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `model_variant`
--

DROP TABLE IF EXISTS `model_variant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `model_variant` (
  `REF_ID` bigint NOT NULL,
  `Base_Variant` varchar(255) DEFAULT NULL,
  `Model_Variant` varchar(255) DEFAULT NULL,
  `Unit_Rec` bigint DEFAULT NULL,
  `Unit_Onhand` bigint DEFAULT NULL,
  `Unit_Sold` bigint DEFAULT NULL,
  PRIMARY KEY (`REF_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `model_variant`
--

LOCK TABLES `model_variant` WRITE;
/*!40000 ALTER TABLE `model_variant` DISABLE KEYS */;
INSERT INTO `model_variant` VALUES (100135,'Sharpener','DOMS Blue',NULL,NULL,NULL),(100235,'Sharpener','DOMS red',NULL,NULL,NULL),(100360,'Pen','Parker',NULL,NULL,NULL),(100361,'Pen','Reynolds',NULL,NULL,NULL),(100362,'Pen','Montex',NULL,NULL,NULL),(100363,'Pen','Rorito',NULL,NULL,NULL),(100364,'Pen','American Cross',NULL,NULL,NULL),(100431,'KeyBoard','Acer Series 321',NULL,NULL,NULL),(100432,'KeyBoard','Acer Series 500',NULL,NULL,NULL),(100435,'KeyBoard','Acer Series 800',NULL,NULL,NULL),(100535,'Eraser','Apsara Short',NULL,NULL,NULL),(100635,'Eraser','Apsara Long',NULL,NULL,NULL);
/*!40000 ALTER TABLE `model_variant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `package_tracking`
--

DROP TABLE IF EXISTS `package_tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `package_tracking` (
  `vendor_name` varchar(255) DEFAULT NULL,
  `base_variant` varchar(255) DEFAULT NULL,
  `model_variant` varchar(255) DEFAULT NULL,
  `Unit_Onhand` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `package_tracking`
--

LOCK TABLES `package_tracking` WRITE;
/*!40000 ALTER TABLE `package_tracking` DISABLE KEYS */;
INSERT INTO `package_tracking` VALUES ('Oynx','Keyboard','Acer 500 Series',480),('Alissa','Keyboard','Acer 300 Series',400),('Anya','Keyboard','Dell Silent 200',250),('Anya','Keyboard','Dell Silent 400',250),('Eren','Pins','Red Small',1000),('Jeager','Pins','Red Big',1500),('Ron','Pins','Blue Big',100),('Ronny','Pins','Blue Smoll',1000),('Phronze','Sharpener','Apsara',1000),('Jubilee','Sharpener','Camlin',1000),('Yogen','Eraser','DOMS',250),('Roman','Eraser','Reynolds',2150);
/*!40000 ALTER TABLE `package_tracking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sold_tracking`
--

DROP TABLE IF EXISTS `sold_tracking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sold_tracking` (
  `customer_name` varchar(255) DEFAULT NULL,
  `base_variant` varchar(255) DEFAULT NULL,
  `model_variant` varchar(255) DEFAULT NULL,
  `quan` int DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sold_tracking`
--

LOCK TABLES `sold_tracking` WRITE;
/*!40000 ALTER TABLE `sold_tracking` DISABLE KEYS */;
INSERT INTO `sold_tracking` VALUES ('Cust 1','KeyBoard','Acer 500 Series',20,50);
/*!40000 ALTER TABLE `sold_tracking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-13 18:26:51
