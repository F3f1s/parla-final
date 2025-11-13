import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Função para inicializar o banco SQLite3.
    # Criação das tabelas User e Post com relacionamento 1:N.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            genero TEXT,
            email TEXT NOT NULL,
            senha TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Post (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES User (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Atividade (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tentativas INTEGER,
            dificuldade TEXT,
            horario TEXT,
            erros INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Personagem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            sapato INTEGER,
            acessorios INTEGER,
            roupa INTEGER,
            cabelo INTEGER,
            corpo INTEGER,
            FOREIGN KEY (usuario_id) REFERENCES User (id)
        )
    ''')

    conn.commit()
    conn.close()