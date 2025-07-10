CREATE DATABASE SISTEMA_AEROPORTO;
USE SISTEMA_AEROPORTO;

CREATE TABLE AEROPORTO(
	CODA varchar(4),
    nome varchar(40),
    cidade varchar(20),
    pais char(2),
    ano_de_abertura int(4),
    
    PRIMARY KEY(CODA)
);

CREATE TABLE PILOTO(
	CODP int(4),
    nomep varchar(40),
    salario float(6,2),
    gratificacoes varchar(50),
    tempo time,
    pais char(2),
    companhia varchar(40),
    
    PRIMARY KEY(CODP)
);
    

describe AEROPORTO;
describe PILOTO;
drop table AEROPORTO;