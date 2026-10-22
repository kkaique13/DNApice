CREATE DATABASE DNAPICE;
USE DNAPICE;
CREATE TABLE bioma (
    id_bioma INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    temperatura DECIMAL(5, 2)
);

CREATE TABLE organismo (
    id_organismo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tempo_sol DECIMAL(8, 2),
    temperatura DECIMAL(5, 2),
    taxa_desidratacao DECIMAL(8, 2),
    energia DECIMAL(8, 2),
    cantil DECIMAL(8, 2),
    hidratacao DECIMAL(8, 2),
    id_bioma INT NOT NULL,

    CONSTRAINT fk_organismo_bioma
        FOREIGN KEY (id_bioma)
        REFERENCES bioma (id_bioma)
);

CREATE TABLE coracao (
    id_coracao INT AUTO_INCREMENT PRIMARY KEY,
    frequencia_cardiaca INT,
    id_organismo INT NOT NULL UNIQUE,

    CONSTRAINT fk_coracao_organismo
        FOREIGN KEY (id_organismo)
        REFERENCES organismo (id_organismo)
);

CREATE TABLE pulmao (
    id_pulmao INT AUTO_INCREMENT PRIMARY KEY,
    oxigenacao DECIMAL(5, 2),
    id_organismo INT NOT NULL UNIQUE,

    CONSTRAINT fk_pulmao_organismo
        FOREIGN KEY (id_organismo)
        REFERENCES organismo (id_organismo)
);