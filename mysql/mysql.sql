create database if exist test;

use test;

CREATE TABLE `test`.`buy_info` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `year` INT NULL,
  `month` INT NULL,
  `day` INT NULL,
  `money` VARCHAR(45) NULL,
  `polt` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  `way` VARCHAR(45) NULL,
  `info` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


insert buy_info(year,month,day,money,polt,type,way,info) value
('2020','12','1','322.1','淘宝','衣服','支付宝','忘记了'),
('2020','12','2','322.1','淘宝','食物','微信','忘记了'),
('2020','12','3','322.1','京东','衣服','支付宝','买错了'),
('2020','12','1','322.1','淘宝','食物','支付宝','买多了');