CREATE DATABASE DB_GabbiCell;

use DB_GabbiCell;

CREATE TABLE Tab_FUNCIONARIO(
ID BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
Nome_Func VARCHAR(75) NOT NULL,
Login_Func varchar(20) UNIQUE NOT NULL,
Senha_Func VARCHAR(20) UNIQUE NOT NULL,
Cargo VARCHAR(25),
Acesso boolean not null
);

CREATE TABLE Tab_Evento(
ID BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
Data_Evento Datetime not null,
Titulo varchar(30) not null,
Descricao varchar(500),
Local varchar(150)
);

CREATE TABLE Tab_Relatorio(
ID_Relatorio BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
Descricao varchar(500),
Categoria varchar(30) NOT NULL,
Data_Periodo Datetime not null
);

CREATE TABLE Tab_ORCAMENTO(
Cod_Orcamento BIGINT PRIMARY KEY NOT NULL,
Nome_Cliente varchar(100) NOT NULL,
Telefone_Cliente varchar(20) NOT NULL,
Documento_Cliente varchar(15) NOT NULL,
Endereco_Cliente varchar(200) NOT NULL,
Aparelho varchar(50) NOT NULL,
Marca varchar(20) NOT NULL,
IMEI VARCHAR(25) NOT NULL,
Reclamacao varchar(200),
Responsavel_Retirada varchar(35) NOT NULL,
Data_Entrada DATETIME NOT NULL,
Data_Saida DATETIME NOT NULL,
Valor_Sinal varchar(10) not null,
Valor_M_Obra varchar(10) not null,
Valor_Peca varchar(10) not null,
Valor_Total varchar(10) not null
);

CREATE TABLE Tab_Produto(
Nome varchar(100) not null,
Cod_Produto BIGINT PRIMARY KEY NOT NULL,
Descricao varchar(100) not null,
Quantidade INT NOT NULL,
Categoria varchar(50),
Marca varchar(20),
Fornecedor varchar(30),
Valor varchar(10) not null
);

CREATE TABLE Tab_Venda(
ID_Venda BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
Valor_Total varchar(10) not null,
Cliente varchar(100) NOT NULL,
Documento_Cliente varchar(15) NOT NULL,
ID_Func BIGINT NOT NULL,
Cod_Produto BIGINT NOT NULL,
Quantidade INT NOT NULL,
Data datetime not null
);

CREATE TABLE Tab_Estoque(
Cod_Produto BIGINT NOT NULL,
Quantidade INT NOT NULL
);

Create table Tab_Recibo(
ID_Venda BIGINT NOT NULL ,
Desconto varchar(10) not null
);