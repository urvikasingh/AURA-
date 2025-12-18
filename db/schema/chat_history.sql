-- Safe DB + table creation for AURA

IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'aura_db')
BEGIN
    CREATE DATABASE aura_db;
END
GO

USE aura_db;
GO

IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME = 'chat_history'
)
BEGIN
    CREATE TABLE chat_history (
        id INT IDENTITY(1,1) PRIMARY KEY,
        user_id INT NULL,
        ai_type NVARCHAR(50) NOT NULL,
        session_id NVARCHAR(100) NULL,
        question NVARCHAR(MAX) NOT NULL,
        answer NVARCHAR(MAX) NOT NULL,
        created_at DATETIME DEFAULT GETDATE()
    );
END
GO
