import sqlite3

def create_post(user_id, title, content):
    """Crie uma nova postagem para o usuário dado."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Post (user_id, title, content) VALUES (?, ?, ?)', (user_id, title, content))
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
    return post_id

def get_post_by_id(post_id):
    """Busque um post pelo seu ID."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Post WHERE id = ?', (post_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'id': row[0],
            'title': row[1],
            'content': row[2],
            'user_id': row[3]
        }
    return None

def get_posts_by_user(user_id):
    """Recupere todas as postagens para o usuário dado."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Post WHERE user_id = ?', (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [
        {'id': r[0], 'title': r[1], 'content': r[2], 'user_id': r[3]}
        for r in rows
    ]

def get_all_posts():
    """Buscar todas as postagens."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Post')
    rows = cursor.fetchall()
    conn.close()
    return [
        {'id': r[0], 'title': r[1], 'content': r[2], 'user_id': r[3]}
        for r in rows
    ]

def update_post(post_id, title, content):
    """Atualizar um post existente."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE Post SET title=?, content=? WHERE id=?', (title, content, post_id))
    conn.commit()
    conn.close()

def delete_post(post_id):
    """Excluir um post do banco de dados."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Post WHERE id=?', (post_id,))
    conn.commit()
    conn.close()

# Funções para criar, buscar por ID, buscar por usuário, buscar todos, atualizar e deletar posts.
# Usa tabela 'Post' e banco 'database.db'.