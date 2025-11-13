import sqlite3

def create_user(nome, idade, genero, email, senha):
    """Create a new user in the database."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO User (nome, idade, genero, email, senha) VALUES (?, ?, ?, ?, ?)', 
                   (nome, idade, genero, email, senha))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

def get_user_by_id(user_id):
    """Fetch a user by their ID."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_all_users():
    """Fetch all users."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM User')
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(user_id, nome, idade, email):
    """Update an existing user."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE User SET nome=?, idade=?, email=? WHERE id=?', (nome, idade, email, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    """Delete a user from the database."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM User WHERE id=?', (user_id,))
    conn.commit()
    conn.close()

# Funções para criar usuário, buscar por ID, buscar todos, atualizar e deletar.
# Usa tabela 'User'.