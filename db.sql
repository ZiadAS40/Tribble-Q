-- prepares a MySQL server for the project
DROP DATABASE IF EXISTS lt_store;
CREATE DATABASE IF NOT EXISTS `tripple_q`;
CREATE USER IF NOT EXISTS 'ziad4036'@'localhost' IDENTIFIED BY 'qqq';
GRANT ALL PRIVILEGES ON `tripple_q`.* TO 'ziad4036'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ziad4036'@'localhost';
FLUSH PRIVILEGES;
