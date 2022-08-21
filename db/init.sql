use urlshortener;

CREATE TABLE test_table (
  name VARCHAR(20),
  color VARCHAR(10)
);

CREATE TABLE input_output(id int NOT NULL AUTO_INCREMENT,inputargs varchar(45) DEFAULT NULL,output varchar(45) DEFAULT NULL,operationtype varchar(45) DEFAULT NULL,PRIMARY KEY (id))
INSERT INTO input_output(inputargs, output,operationtype)VALUES  ('/0/0', '0','addition');
  

INSERT INTO test_table
  (name, color)
VALUES
  ('dev', 'blue'),
  ('pro', 'yellow');