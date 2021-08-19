-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: MOVIE_STUDIO
-- ------------------------------------------------------
-- Server version	8.0.21-0ubuntu0.20.04.4

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
-- Table structure for table `Actor`
--
DROP DATABASE IF EXISTS MOVIE_STUDIO;
CREATE SCHEMA MOVIE_STUDIO;
USE MOVIE_STUDIO;

DROP TABLE IF EXISTS `Actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actor` (
  `Aadhar_ID` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `DOB` date DEFAULT NULL,
  `Contact` varchar(30) NOT NULL,
  `Remuneration` float NOT NULL,
  `Leadflag` tinyint(1) NOT NULL,
  `Filmography` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`Aadhar_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor`
--

LOCK TABLES `Actor` WRITE;
/*!40000 ALTER TABLE `Actor` DISABLE KEYS */;
INSERT INTO `Actor` VALUES (31741,'Jaffa','1943-02-19','1213392',23,1,2),(1924723,'Robert Downey',NULL,'262347',50,1,9),(1947263,'Vadivelu',NULL,'2942847',2,0,10),(2846283,'Emma Watson','1996-08-22','2782377',15,0,3),(4298793,'Thaliwa','1967-02-13','232347',35,1,7),(72465872,'Priyanka Chopra','1950-06-12','17392',1,1,12);
/*!40000 ALTER TABLE `Actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Actor_Accolades`
--

DROP TABLE IF EXISTS `Actor_Accolades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actor_Accolades` (
  `Aadhar_ID` int DEFAULT NULL,
  `Name_of_Accolade` varchar(30) DEFAULT NULL,
  KEY `Aadhar_ID` (`Aadhar_ID`),
  CONSTRAINT `Actor_Accolades_ibfk_1` FOREIGN KEY (`Aadhar_ID`) REFERENCES `Actor` (`Aadhar_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor_Accolades`
--

LOCK TABLES `Actor_Accolades` WRITE;
/*!40000 ALTER TABLE `Actor_Accolades` DISABLE KEYS */;
INSERT INTO `Actor_Accolades` VALUES (31741,'FILMAFARE BEST COMEDIAN'),(72465872,'MISS UNIVERESE'),(4298793,'PADMABHUSHAN'),(1924723,'Oscar'),(4298793,'NATIONAL AWARD'),(2846283,'Oscar'),(1947263,NULL);
/*!40000 ALTER TABLE `Actor_Accolades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Actor_Address_City`
--

DROP TABLE IF EXISTS `Actor_Address_City`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actor_Address_City` (
  `Aadhar_ID` int DEFAULT NULL,
  `City` varchar(30) DEFAULT NULL,
  KEY `Aadhar_ID` (`Aadhar_ID`),
  CONSTRAINT `Actor_Address_City_ibfk_1` FOREIGN KEY (`Aadhar_ID`) REFERENCES `Actor` (`Aadhar_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor_Address_City`
--

LOCK TABLES `Actor_Address_City` WRITE;
/*!40000 ALTER TABLE `Actor_Address_City` DISABLE KEYS */;
INSERT INTO `Actor_Address_City` VALUES (31741,'Hyderabad'),(1924723,'Sydney'),(1947263,'Chennai'),(2846283,'London'),(4298793,'Mumbai'),(72465872,'Delhi');
/*!40000 ALTER TABLE `Actor_Address_City` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Actor_Address_Country`
--

DROP TABLE IF EXISTS `Actor_Address_Country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actor_Address_Country` (
  `Aadhar_ID` int DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  `Country` varchar(30) DEFAULT NULL,
  CONSTRAINT `Actor_Address_Country_ibfk_1` FOREIGN KEY (`Aadhar_ID`) REFERENCES `Actor` (`Aadhar_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor_Address_Country`
--

LOCK TABLES `Actor_Address_Country` WRITE;
/*!40000 ALTER TABLE `Actor_Address_Country` DISABLE KEYS */;
INSERT INTO `Actor_Address_Country` VALUES (31741,'Telangana','India'),(1924723,'New South Wales','Australia'),(1947263,'Tamil Nadu','India'),(2846283,'United Kingdom','England'),(4298793,'Maharashtra','India'),(72465872,'New Delhi','India');
/*!40000 ALTER TABLE `Actor_Address_Country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Actor_Address_State`
--

DROP TABLE IF EXISTS `Actor_Address_State`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actor_Address_State` (
  `Aadhar_ID` int DEFAULT NULL,
  `City` varchar(30) DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  CONSTRAINT `Actor_Address_State_ibfk_1` FOREIGN KEY (`Aadhar_ID`) REFERENCES `Actor` (`Aadhar_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor_Address_State`
--

LOCK TABLES `Actor_Address_State` WRITE;
/*!40000 ALTER TABLE `Actor_Address_State` DISABLE KEYS */;
INSERT INTO `Actor_Address_State` VALUES (31741,'Hyderabad','Telangana'),(1924723,'Sydney','New South Wales'),(1947263,'Chennai','Tamil Nadu'),(2846283,'London','United Kingdom'),(4298793,'Mumbai','Maharashtra'),(72465872,'Delhi','New Delhi');
/*!40000 ALTER TABLE `Actor_Address_State` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `COORDINATES_WITH`
--

DROP TABLE IF EXISTS `COORDINATES_WITH`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `COORDINATES_WITH` (
  `Director_ID` int NOT NULL,
  `Movie_ID` int NOT NULL,
  KEY `Director_ID` (`Director_ID`),
  KEY `Movie_ID` (`Movie_ID`),
  CONSTRAINT `COORDINATES_WITH_ibfk_1` FOREIGN KEY (`Director_ID`) REFERENCES `Director` (`Director_ID`),
  CONSTRAINT `COORDINATES_WITH_ibfk_2` FOREIGN KEY (`Movie_ID`) REFERENCES `VFX` (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `COORDINATES_WITH`
--

LOCK TABLES `COORDINATES_WITH` WRITE;
/*!40000 ALTER TABLE `COORDINATES_WITH` DISABLE KEYS */;
INSERT INTO `COORDINATES_WITH` VALUES (20161,2019101040),(20161,2019101087),(20162,2019101043),(201602,2019101043),(2016002,2019111019),(201601,2019111012),(20162,2019111009);
/*!40000 ALTER TABLE `COORDINATES_WITH` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Director`
--

DROP TABLE IF EXISTS `Director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Director` (
  `Director_ID` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `DOB` date DEFAULT NULL,
  `Filmography` int NOT NULL,
  `Mainflag` tinyint(1) NOT NULL,
  `MainID` int DEFAULT NULL,
  PRIMARY KEY (`Director_ID`),
  KEY `MainID` (`MainID`),
  CONSTRAINT `Director_ibfk_1` FOREIGN KEY (`MainID`) REFERENCES `Director` (`Director_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Director`
--

LOCK TABLES `Director` WRITE;
/*!40000 ALTER TABLE `Director` DISABLE KEYS */;
INSERT INTO `Director` VALUES (145,'vetrimaran','2000-09-29',21,1,NULL),(20161,'Shankar','1957-05-06',24,1,NULL),(20162,'James Cameroon','1951-11-13',2,1,NULL),(201601,'Ravi teja','1973-06-01',16,0,20161),(201602,'V.V.Vinayak','1963-12-29',35,0,20162),(2016002,'RGV','1954-10-14',16,0,201602);
/*!40000 ALTER TABLE `Director` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Director_Accolades`
--

DROP TABLE IF EXISTS `Director_Accolades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Director_Accolades` (
  `Director_ID` int NOT NULL,
  `Name_of_Accolade` varchar(30) DEFAULT NULL,
  KEY `Director_ID` (`Director_ID`),
  CONSTRAINT `Director_Accolades_ibfk_1` FOREIGN KEY (`Director_ID`) REFERENCES `Director` (`Director_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Director_Accolades`
--

LOCK TABLES `Director_Accolades` WRITE;
/*!40000 ALTER TABLE `Director_Accolades` DISABLE KEYS */;
INSERT INTO `Director_Accolades` VALUES (20161,'FILMFARE'),(20162,'OSCAR'),(201601,'NANDI'),(201602,NULL),(2016002,'JAFFA'),(2016002,'PADMASRI'),(145,'Best');
/*!40000 ALTER TABLE `Director_Accolades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Director_Address_City`
--

DROP TABLE IF EXISTS `Director_Address_City`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Director_Address_City` (
  `Director_ID` int DEFAULT NULL,
  `City` varchar(30) DEFAULT NULL,
  KEY `Director_ID` (`Director_ID`),
  CONSTRAINT `Director_Address_City_ibfk_1` FOREIGN KEY (`Director_ID`) REFERENCES `Director` (`Director_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Director_Address_City`
--

LOCK TABLES `Director_Address_City` WRITE;
/*!40000 ALTER TABLE `Director_Address_City` DISABLE KEYS */;
INSERT INTO `Director_Address_City` VALUES (20161,'Chennai'),(20162,'Los Angeles'),(201601,'Hyderabad'),(201602,'Tirupati'),(2016002,'Bhubaneshwar');
/*!40000 ALTER TABLE `Director_Address_City` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Director_Address_Country`
--

DROP TABLE IF EXISTS `Director_Address_Country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Director_Address_Country` (
  `Director_ID` int DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  `Country` varchar(30) DEFAULT NULL,
  CONSTRAINT `Director_Address_Country_ibfk_1` FOREIGN KEY (`Director_ID`) REFERENCES `Director` (`Director_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Director_Address_Country`
--

LOCK TABLES `Director_Address_Country` WRITE;
/*!40000 ALTER TABLE `Director_Address_Country` DISABLE KEYS */;
INSERT INTO `Director_Address_Country` VALUES (20161,'Tamil Nadu','India'),(20162,'California','USA'),(201601,'Telangana','India'),(201602,'Andhra Pradesh','India'),(2016002,'Orissa','India');
/*!40000 ALTER TABLE `Director_Address_Country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Director_Address_State`
--

DROP TABLE IF EXISTS `Director_Address_State`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Director_Address_State` (
  `Director_ID` int DEFAULT NULL,
  `City` varchar(30) DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  CONSTRAINT `Director_Address_State_ibfk_1` FOREIGN KEY (`Director_ID`) REFERENCES `Director` (`Director_ID`) ON DELETE CASCADE

  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Director_Address_State`
--

LOCK TABLES `Director_Address_State` WRITE;
/*!40000 ALTER TABLE `Director_Address_State` DISABLE KEYS */;
INSERT INTO `Director_Address_State` VALUES (20161,'Chennai','Tamil Nadu'),(20162,'Los Angeles','California'),(201601,'Hyderabad','Telangana'),(201602,'Tirupati','Andhra Pradesh'),(2016002,'Bhubaneshwar','Orissa');
/*!40000 ALTER TABLE `Director_Address_State` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie_Awards`
--

DROP TABLE IF EXISTS `Movie_Awards`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie_Awards` (
  `Movie_ID` int NOT NULL,
  `Award_Name` varchar(30) DEFAULT NULL,
  KEY `Movie_ID` (`Movie_ID`),
  CONSTRAINT `Movie_Awards_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie_Awards`
--

LOCK TABLES `Movie_Awards` WRITE;
/*!40000 ALTER TABLE `Movie_Awards` DISABLE KEYS */;
INSERT INTO `Movie_Awards` VALUES (2019101040,'FILMFARE'),(2019101087,'OSCAR'),(2019101043,'NANDI'),(2019111012,'NATIONAL AWARD'),(2019101087,'FILMFARE'),(2019111019,NULL),(2019111009,'OSCAR');
/*!40000 ALTER TABLE `Movie_Awards` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie_Collections`
--

DROP TABLE IF EXISTS `Movie_Collections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie_Collections` (
  `Movie_ID` int NOT NULL,
  `Collections` int DEFAULT NULL,
  KEY `Movie_ID` (`Movie_ID`),
  CONSTRAINT `Movie_Collections_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie_Collections`
--

LOCK TABLES `Movie_Collections` WRITE;
/*!40000 ALTER TABLE `Movie_Collections` DISABLE KEYS */;
INSERT INTO `Movie_Collections` VALUES (2019101040,200),(2019101043,50),(2019101087,80),(2019111012,120),(2019111009,10000),(2019111019,70),(2019111001, 582);
/*!40000 ALTER TABLE `Movie_Collections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie_Profit_or_Loss`
--

DROP TABLE IF EXISTS `Movie_Profit_or_Loss`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie_Profit_or_Loss` (
  `Movie_ID` int NOT NULL,
  `Profit_or_Loss` int DEFAULT NULL,
  KEY `Movie_ID` (`Movie_ID`),
  CONSTRAINT `Movie_Profit_or_Loss_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie_Profit_or_Loss`
--

LOCK TABLES `Movie_Profit_or_Loss` WRITE;
/*!40000 ALTER TABLE `Movie_Profit_or_Loss` DISABLE KEYS */;
INSERT INTO `Movie_Profit_or_Loss` VALUES (2019101040,20),(2019101043,35),(2019101087,-16),(2019111009,572),(2019111012,13),(2019111019,NULL),(2019111001, 450);
/*!40000 ALTER TABLE `Movie_Profit_or_Loss` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie_info`
--

DROP TABLE IF EXISTS `Movie_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie_info` (
  `Movie_ID` int NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Release_Date` date DEFAULT NULL,
  `Avg_rate` double DEFAULT NULL,
  `Budget` int NOT NULL,
  `Director_ID` int NOT NULL,
  `Film_No` int NOT NULL,
  PRIMARY KEY (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie_info`
--

LOCK TABLES `Movie_info` WRITE;
/*!40000 ALTER TABLE `Movie_info` DISABLE KEYS */;
INSERT INTO `Movie_info` VALUES (2019101040,'Sarrainodu','2002-05-23',4.672,30,868892,2),(2019101043,'Charlie','2001-09-21',5,15,136892,3),(2019101087,'HARRY POTTER PART-1','2002-09-22',4.5,50,86887,1),(2019111009,'Avengers','2008-03-12',5,1000,4262892,5),(2019111012,'Android Kunjappan','2002-06-14',4.7,60,2312892,4),(2019111019,'HARRYPOTTER PART-9',NULL,NULL,120,4262832,6),(2019111001, "Robo", '2010-10-01', 4.2, 132, 20161, 18);
/*!40000 ALTER TABLE `Movie_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `REQUIRES`
--

DROP TABLE IF EXISTS `REQUIRES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `REQUIRES` (
  `Aadhar_ID` int NOT NULL,
  `Director_ID` int NOT NULL,
  `Movie_ID` int NOT NULL,
  `SET_ID` int NOT NULL,
  KEY `Aadhar_ID` (`Aadhar_ID`),
  KEY `Director_ID` (`Director_ID`),
  KEY `Movie_ID` (`Movie_ID`),
  KEY `SET_ID` (`SET_ID`),
  CONSTRAINT `REQUIRES_ibfk_1` FOREIGN KEY (`Aadhar_ID`) REFERENCES `Actor` (`Aadhar_ID`),
  CONSTRAINT `REQUIRES_ibfk_2` FOREIGN KEY (`Director_ID`) REFERENCES `Director` (`Director_ID`),
  CONSTRAINT `REQUIRES_ibfk_3` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`),
  CONSTRAINT `REQUIRES_ibfk_4` FOREIGN KEY (`SET_ID`) REFERENCES `Set_Location` (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `REQUIRES`
--

LOCK TABLES `REQUIRES` WRITE;
/*!40000 ALTER TABLE `REQUIRES` DISABLE KEYS */;
INSERT INTO `REQUIRES` VALUES (1924723,20161,2019101040,2019101040),(1947263,20161,2019101040,2019101040),(1947263,20162,2019101043,2019101043),(2846283,201602,2019101087,2019101087),(2846283,2016002,2019111009,2019101087),(4298793,201601,2019111019,2019111019);
/*!40000 ALTER TABLE `REQUIRES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Set_Cost`
--

DROP TABLE IF EXISTS `Set_Cost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Set_Cost` (
  `Movie_ID` int NOT NULL,
  `Cost` int DEFAULT NULL,
  `VFX_ID` int NOT NULL,
  `Location_Depicted` varchar(30) DEFAULT NULL,
  UNIQUE KEY `Movie_ID_2` (`Movie_ID`,`Location_Depicted`),
  KEY `Movie_ID` (`Movie_ID`),
  KEY `VFX_ID` (`VFX_ID`),
  CONSTRAINT `Set_Cost_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`),
  CONSTRAINT `Set_Cost_ibfk_2` FOREIGN KEY (`VFX_ID`) REFERENCES `VFX` (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Set_Cost`
--

LOCK TABLES `Set_Cost` WRITE;
/*!40000 ALTER TABLE `Set_Cost` DISABLE KEYS */;
INSERT INTO `Set_Cost` VALUES (2019101040,30,2019101040,'Italy'),(2019101043,2,2019101043,'Africa'),(2019101087,11,2019101087,'Australia'),(2019111009,6,2019111009,'Hyderabad'),(2019111019,15,2019111019,'Sydney'),(2019111012,1,2019111012,'jurassic park');
/*!40000 ALTER TABLE `Set_Cost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Set_Location`
--

DROP TABLE IF EXISTS `Set_Location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Set_Location` (
  `Movie_ID` int NOT NULL,
  `Location_Depicted` varchar(30) NOT NULL,
  `VFX_ID` int NOT NULL,
  UNIQUE KEY `Movie_ID_2` (`Movie_ID`,`Location_Depicted`),
  KEY `VFX_ID` (`VFX_ID`),
  CONSTRAINT `Set_Location_ibfk_2` FOREIGN KEY (`VFX_ID`) REFERENCES `VFX` (`Movie_ID`),
  CONSTRAINT `Set_Location_ibfk_3` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Set_Location`
--

LOCK TABLES `Set_Location` WRITE;
/*!40000 ALTER TABLE `Set_Location` DISABLE KEYS */;
INSERT INTO `Set_Location` VALUES (2019101040,'Italy',2019101040),(2019101043,'Africa',2019101043),(2019101087,'Australia',2019101087),(2019111009,'Hyderabad',2019111009),(2019111012,'jurassic park',2019111012),(2019111019,'Sydney',2019111019);
/*!40000 ALTER TABLE `Set_Location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Set_Manpower`
--

DROP TABLE IF EXISTS `Set_Manpower`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Set_Manpower` (
  `Movie_ID` int NOT NULL,
  `Man_Power` int DEFAULT NULL,
  `VFX_ID` int NOT NULL,
  `Location_Depicted` varchar(30) DEFAULT NULL,
  UNIQUE KEY `Movie_ID_2` (`Movie_ID`,`Location_Depicted`),
  KEY `Movie_ID` (`Movie_ID`),
  KEY `VFX_ID` (`VFX_ID`),
  CONSTRAINT `Set_Manpower_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`),
  CONSTRAINT `Set_Manpower_ibfk_2` FOREIGN KEY (`VFX_ID`) REFERENCES `VFX` (`Movie_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Set_Manpower`
--

LOCK TABLES `Set_Manpower` WRITE;
/*!40000 ALTER TABLE `Set_Manpower` DISABLE KEYS */;
INSERT INTO `Set_Manpower` VALUES (2019111019,20,2019111019,'Sydney'),(2019111012,300,2019111012,'jurassic park'),(2019111009,NULL,2019111009,'Hyderabad'),(2019101087,36,2019101087,'Australia'),(2019101043,43,2019101043,'Africa'),(2019101040,22,2019101040,'Italy');
/*!40000 ALTER TABLE `Set_Manpower` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VFX`
--

DROP TABLE IF EXISTS `VFX`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `VFX` (
  `VFX_Director` varchar(30) NOT NULL,
  `Avg_Demand` float DEFAULT NULL,
  `Name` varchar(30) NOT NULL,
  `Movie_ID` int NOT NULL,
  UNIQUE KEY `Movie_ID_2` (`Movie_ID`),
  KEY `Movie_ID` (`Movie_ID`),
  CONSTRAINT `VFX_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `Movie_info` (`Movie_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VFX`
--

LOCK TABLES `VFX` WRITE;
/*!40000 ALTER TABLE `VFX` DISABLE KEYS */;
INSERT INTO `VFX` VALUES ('Harsha redyy',4.12,'Arka',2019101040),('Mohan lal',3.57,'Makuta',2019101043),('Tom cruise',3.67,'Red chillies',2019101087),('Mohan lal',3.57,'Makuta',2019111009),('Tom cruise',3.67,'Red chillies',2019111012),('Harsha redyy',4.12,'Arka',2019111019);
/*!40000 ALTER TABLE `VFX` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VFX_Address_City`
--

DROP TABLE IF EXISTS `VFX_Address_City`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `VFX_Address_City` (
  `Movie_ID` int DEFAULT NULL,
  `City` varchar(30) DEFAULT NULL,
  KEY `Movie_ID` (`Movie_ID`),
  CONSTRAINT `VFX_Address_City_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `VFX` (`Movie_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VFX_Address_City`
--

LOCK TABLES `VFX_Address_City` WRITE;
/*!40000 ALTER TABLE `VFX_Address_City` DISABLE KEYS */;
INSERT INTO `VFX_Address_City` VALUES (2019101040,'Hyderabad'),(2019101043,'Kochi'),(2019101087,'Sydney'),(2019111009,'Los Angeles'),(2019111012,'Chennai'),(2019111019,'Dispur');
/*!40000 ALTER TABLE `VFX_Address_City` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VFX_Address_Country`
--

DROP TABLE IF EXISTS `VFX_Address_Country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `VFX_Address_Country` (
  `Movie_ID` int DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  `Country` varchar(30) DEFAULT NULL,
  CONSTRAINT `VFX_Address_Country_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `VFX` (`Movie_ID`) ON DELETE CASCADE

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VFX_Address_Country`
--

LOCK TABLES `VFX_Address_Country` WRITE;
/*!40000 ALTER TABLE `VFX_Address_Country` DISABLE KEYS */;
INSERT INTO `VFX_Address_Country` VALUES (2019101040,'Telangana','India'),(2019101043,'Kerala','India'),(2019101087,'New South Wales','Australia'),(2019111009,'California','USA'),(2019111012,'Tamil Nadu','India'),(2019111019,'Assam','India');
/*!40000 ALTER TABLE `VFX_Address_Country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `VFX_Address_State`
--

DROP TABLE IF EXISTS `VFX_Address_State`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `VFX_Address_State` (
  `Movie_ID` int DEFAULT NULL,
  `City` varchar(30) DEFAULT NULL,
  `State` varchar(30) DEFAULT NULL,
  CONSTRAINT `VFX_Address_State_ibfk_1` FOREIGN KEY (`Movie_ID`) REFERENCES `VFX` (`Movie_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `VFX_Address_State`
--

LOCK TABLES `VFX_Address_State` WRITE;
/*!40000 ALTER TABLE `VFX_Address_State` DISABLE KEYS */;
INSERT INTO `VFX_Address_State` VALUES (2019101040,'Hyderabad','Telangana'),(2019101043,'Kochi','Kerala'),(2019101087,'Sydney','New South Wales'),(2019111009,'Los Angeles','California'),(2019111012,'Chennai','Tamil Nadu'),(2019111019,'Dispur','Assam');
/*!40000 ALTER TABLE `VFX_Address_State` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-04 19:48:33
