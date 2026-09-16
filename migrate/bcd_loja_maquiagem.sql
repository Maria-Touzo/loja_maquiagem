CREATE DATABASE IF NOT EXISTS  db_loja_maquiagem;
USE db_loja_maquiagem;

CREATE TABLE  IF NOT EXISTS tb_categorias (
 id_categoria INT AUTO_INCREMENT PRIMARY KEY,
 nome_categoria VARCHAR(40)
);

CREATE TABLE  IF NOT EXISTS tb_produtos (
 id_produto INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 id_categoria INT NOT NULL,
 nome_produto VARCHAR(50) NOT NULL,
 descricao VARCHAR(200),
 preco DECIMAL(10,2) NOT NULL
);



CREATE TABLE  IF NOT EXISTS tb_produtos_imagens (
 id_imagem INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 id_produto INT NOT NULL,
 url_imagem VARCHAR(255)
);

CREATE TABLE  IF NOT EXISTS tb_usuarios (
 id_usuario INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 nome VARCHAR(150) ,
 email NOT NULL UNIQUE VARCHAR(150) ,
 telefone VARCHAR(20),
 senha NOT NULL VARCHAR(10),
 endereco VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS tb_comentarios (
 id_comentario INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 id_produto INT NOT NULL,
 id_usuario INT NOT NULL,
 texto VARCHAR(100),
 data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE tb_produtos ADD CONSTRAINT FK_tb_produtos FOREIGN KEY (id_categoria) REFERENCES tb_categorias (id_categoria);
ALTER TABLE tb_produtos_imagens ADD CONSTRAINT FK_tb_produtos_imagens_0 FOREIGN KEY (id_produto) REFERENCES tb_produtos (id_produto);
ALTER TABLE tb_comentarios ADD CONSTRAINT FK_tb_comentarios_0 FOREIGN KEY (id_produto) REFERENCES tb_produtos (id_produto);
ALTER TABLE tb_comentarios ADD CONSTRAINT FK_tb_comentarios_1 FOREIGN KEY (id_usuario) REFERENCES tb_usuarios (id_usuario);

INSERT INTO tb_usuarios(nome, email, telefone, senha, endereco)
 VALUES('maju', 'maju.t@gmail.com', '(16) 998765544', 'maju12', 'rua das dores');
