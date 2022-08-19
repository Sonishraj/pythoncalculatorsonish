create database devopsroles;
use devopsroles;

CREATE TABLE test_table (
  name VARCHAR(20),
  color VARCHAR(10)
);

CREATE TABLE input_output (
  id int NOT NULL AUTO_INCREMENT,
  inputargs varchar(45) DEFAULT NULL,
  output varchar(45) DEFAULT NULL,
  operationtype varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
);

INSERT INTO test_table
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow');