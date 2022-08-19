create database pythoncalc;
use pythoncalc;

CREATE TABLE test_table (
  name VARCHAR(20),
  color VARCHAR(10)
);

CREATE TABLE `input_output` (
  `id` int NOT NULL AUTO_INCREMENT,
  `inputargs` varchar(45) DEFAULT NULL,
  `output` varchar(45) DEFAULT NULL,
  `operationtype` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO test_table
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow');