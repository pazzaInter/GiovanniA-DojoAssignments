CREATE DATABASE  IF NOT EXISTS `emails` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `emails`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: emails
-- ------------------------------------------------------
-- Server version	5.6.34-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `emails`
--

DROP TABLE IF EXISTS `emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email_address` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emails`
--

LOCK TABLES `emails` WRITE;
/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
INSERT INTO `emails` VALUES (1,'test@gmail.com','2017-04-25 21:40:53','2017-04-25 21:40:53'),(2,'test@gmail.com','2017-04-25 21:42:01','2017-04-25 21:42:01'),(3,'test2@gmail.com','2017-04-25 21:43:09','2017-04-25 21:43:09'),(4,'test3@gmail.com','2017-04-25 21:45:53','2017-04-25 21:45:53'),(5,'test3@gmail.com','2017-04-25 21:45:53','2017-04-25 21:45:53'),(6,'test4@gmail.com','2017-04-25 21:48:28','2017-04-25 21:48:28'),(7,'test4@gmail.com','2017-04-25 21:49:41','2017-04-25 21:49:41'),(8,'test4@gmail.com','2017-04-25 21:52:18','2017-04-25 21:52:18'),(9,'test4@gmail.com','2017-04-25 21:54:38','2017-04-25 21:54:38'),(10,'test4@gmail.com','2017-04-25 21:55:35','2017-04-25 21:55:35'),(11,'test4@gmail.com','2017-04-25 21:56:28','2017-04-25 21:56:28'),(12,'test4@gmail.com','2017-04-25 21:57:24','2017-04-25 21:57:24'),(13,'test4@gmail.com','2017-04-25 21:57:50','2017-04-25 21:57:50'),(14,'test7@gmail.com','2017-04-25 22:06:17','2017-04-25 22:06:17');
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-25 22:08:56
