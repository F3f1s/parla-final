import sqlite3

def create_personagem(usuario_id, sapato, acessorios, roupa, cabelo, corpo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Personagem (usuario_id, sapato, acessorios, roupa, cabelo, corpo)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (usuario_id, sapato, acessorios, roupa, cabelo, corpo))
    conn.commit()
    personagem_id = cursor.lastrowid
    conn.close()
    return personagem_id

def get_personagem_by_id(personagem_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Personagem WHERE id = ?', (personagem_id,))
    personagem = cursor.fetchone()
    conn.close()
    return personagem

def get_all_personagens():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Personagem')
    personagens = cursor.fetchall()
    conn.close()
    return personagens

def update_personagem(personagem_id, sapato, acessorios, roupa, cabelo, corpo):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Personagem SET sapato=?, acessorios=?, roupa=?, cabelo=?, corpo=?
        WHERE id=?
    ''', (sapato, acessorios, roupa, cabelo, corpo, personagem_id))
    conn.commit()
    conn.close()

def delete_personagem(personagem_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Personagem WHERE id=?', (personagem_id,))
    conn.commit()
    conn.close()
