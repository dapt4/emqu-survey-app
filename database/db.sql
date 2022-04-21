CREATE DATABASE `socialdb` DEFAULT CHARACTER SET utf8 ;

USE socialdb;

CREATE TABLE `participant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(45) NOT NULL UNIQUE,
  `age` varchar(10) NOT NULL,
  `sex` varchar(10) NOT NULL,
  `favorite` varchar(45) NOT NULL,
  `facebook` int(11) NOT NULL,
  `whatsapp` int(11) NOT NULL,
  `twitter` int(11) NOT NULL,
  `instagram` int(11) NOT NULL,
  `tiktok` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

