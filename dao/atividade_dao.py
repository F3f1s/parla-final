import sqlite3

def create_atividade(tentativas, dificuldade, horario, erros):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Atividade (tentativas, dificuldade, horario, erros) VALUES (?, ?, ?, ?)', 
                   (tentativas, dificuldade, horario, erros))
    conn.commit()
    atividade_id = cursor.lastrowid
    conn.close()
    return atividade_id

def get_atividade_by_id(atividade_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Atividade WHERE id = ?', (atividade_id,))
    atividade = cursor.fetchone()
    conn.close()
    return atividade

def get_all_atividades():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Atividade')
    atividades = cursor.fetchall()
    conn.close()
    return atividades

def update_atividade(atividade_id, tentativas, dificuldade, horario, erros):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Atividade SET tentativas=?, dificuldade=?, horario=?, erros=? WHERE id=?', 
                   (tentativas, dificuldade, horario, erros, atividade_id))
    conn.commit()
    conn.close()

def delete_atividade(atividade_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Atividade WHERE id=?', (atividade_id,))
    conn.commit()
    conn.close()
