
CREATE DATABASE client_query_db;
GO
USE client_query_db;

CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20)
);

CREATE TABLE queries (
    query_id INT IDENTITY(1,1) PRIMARY KEY,
    mail_id VARCHAR(100),
    mobile_number VARCHAR(15),
    query_heading VARCHAR(255),
    query_description VARCHAR(MAX),
    status VARCHAR(20),
    query_created_time DATETIME DEFAULT GETDATE(),
    query_closed_time DATETIME
);
