-- prepares a MySQL server for the project
DROP DATABASE IF EXISTS `tripple_q`;
CREATE DATABASE IF NOT EXISTS `tripple_q`;
GRANT ALL PRIVILEGES ON `tripple_q`.* TO 'ziad4036'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'ziad4036'@'localhost';
FLUSH PRIVILEGES;
