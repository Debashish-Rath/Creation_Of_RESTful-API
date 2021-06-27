-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: the_tech_world_store
-- ------------------------------------------------------
-- Server version	8.0.25

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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `Product_ID` int NOT NULL,
  `Product_Name` varchar(80) DEFAULT NULL,
  `Product_Category_ID` int DEFAULT NULL,
  `Product_Category_Name` varchar(50) DEFAULT NULL,
  `Product_Price` int DEFAULT NULL,
  PRIMARY KEY (`Product_ID`),
  UNIQUE KEY `Product_Name_UNIQUE` (`Product_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Xiaomi Redmi Note 8',1,'Smart Phones',8999),(2,'Lenovo Ideapad gaming 3i',2,'Laptops',64500),(3,'Boat Bassheads 100',4,'Audio Products',399),(4,'Asus VivoBook 15 X513',2,'Laptops',43990),(5,'OnePlus 8T',1,'Smart Phones',39999),(6,'OnePlus 7T',1,'Smart Phones',34999),(7,'Realme X7 Pro',1,'Smart Phones',25999),(8,'OnePlus Bullet Wireless Z',4,'Audio Products',1999),(9,'Zebronics BX53 Bluetooth Speaker',4,'Audio Products',7999),(10,'Boat Stone 1000 Bluetooth HeavyDuty Speaker',4,'Audio Products',1999),(11,'HP Pavilion 14\'\' 360 X576 Model',2,'Laptops',68999),(12,'HP NoteBook FR2005TU 15.6\'\'',2,'Laptops',64999),(13,'Zebronics UPS',3,'Computer Accessories',1499),(14,'Gigabyte Laptop SSD 240 GB',3,'Computer Accessories',3499),(15,'Hynix 4GB DDR3 Desktop RAM',3,'Computer Accessories',1699),(16,'Seagate 1 TB External HDD ',3,'Computer Accessories',3599),(17,'POCO X3 Pro',1,'Smart Phones',21999);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-27 20:57:28
