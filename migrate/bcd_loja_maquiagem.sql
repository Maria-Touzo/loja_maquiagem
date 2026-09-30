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
 preco DECIMAL(10,2) NOT NULL,
 foto_principal VARCHAR(255)
);


CREATE TABLE  IF NOT EXISTS tb_usuarios (
 id_usuario INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
 nome VARCHAR(150) ,
 email VARCHAR(150) NOT NULL UNIQUE  ,
 telefone VARCHAR(20),
 senha VARCHAR(10) NOT NULL ,
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
ALTER TABLE tb_comentarios ADD CONSTRAINT FK_tb_comentarios_0 FOREIGN KEY (id_produto) REFERENCES tb_produtos (id_produto);
ALTER TABLE tb_comentarios ADD CONSTRAINT FK_tb_comentarios_1 FOREIGN KEY (id_usuario) REFERENCES tb_usuarios (id_usuario);

INSERT INTO tb_usuarios(nome, email, telefone, senha, endereco)
 VALUES('maju', 'maju.t@gmail.com', '(16) 998765544', 'maju12', 'rua das dores');
 
 INSERT INTO tb_categorias(nome_categoria)
 VALUES ('blush');
 
INSERT INTO tb_categorias(nome_categoria)
 VALUES ('batom');
 
 INSERT INTO tb_categorias(nome_categoria)
 VALUES ('base');
 
 INSERT INTO tb_produtos(id_categoria, nome_produto, descricao, preco, foto_principal)
 VALUES ('1','blush maju', 'blsuh rosa', '20.00', 'https://i.pinimg.com/474x/9c/8e/13/9c8e131f6fd89e4da71652e4a2adea38.jpg');
 
 INSERT INTO tb_produtos(id_categoria, nome_produto, descricao, preco, foto_principal)
 VALUES ('2','batom vermelho', 'batom vermelho lindo', '10.00', 'https://i.pinimg.com/736x/b5/9f/9b/b59f9bc9ee94eacd514e69acccd7624c.jpg');
 
 INSERT INTO tb_produtos(id_categoria, nome_produto, descricao, preco, foto_principal)
 VALUES ('3','base glow', 'base glow, sua melhor escolha', '40.00', 'https://i.pinimg.com/236x/9c/6e/4b/9c6e4b19b2337d6aad70d2aa87d8fe6c.jpg');
 
 INSERT INTO tb_comentarios(id_produto, id_usuario, texto)
 VALUES ('1', '1', 'lindo esse blush');
