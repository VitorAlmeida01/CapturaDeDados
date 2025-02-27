CREATE user 'insert_user'@'%' identified by 'borainserir123';
GRANT insert on python.dados to 'insert_user'@'%';
GRANT insert on python.maquina to 'insert_user'@'%';
FLUSH privileges;

CREATE user 'select_user'@'%' identified by 'boraselecionar123';
GRANT select on python.dados to 'select_user'@'%';
GRANT select on python.maquina to 'select_user'@'%';
FLUSH privileges;

CREATE DATABASE python;
USE python;
DROP DATABASE python;

CREATE TABLE maquina (
	cod int primary key,
	ram float,
	cpu float,
	disk float
);

CREATE TABLE dados (
    idDados INT PRIMARY KEY AUTO_INCREMENT,
    cpu_percent FLOAT,
    ram_percent FLOAT,
    disk_percent FLOAT,
    cpu_byte FLOAT,
    ram_byte FLOAT,
    disk_byte FLOAT,
    timestamp DATETIME,
    fkMaquina int,
    foreign key (fkMaquina) references maquina (cod)
);
SELECT * FROM maquina;

SELECT cpu_percent FROM dados JOIN maquina on fkMaquina = cod
	WHERE cod = 234;

SELECT AVG(cpu_percent) FROM dados;

