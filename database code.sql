CREATE DATABASE kddlab;
USE kddlab;
CREATE TABLE logininfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
CREATE TABLE summaries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    summary TEXT NOT NULL,
    FOREIGN KEY (username) REFERENCES logininfo(username)
);
