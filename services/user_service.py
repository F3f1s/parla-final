from dao.user_dao import (
    create_user, get_user_by_id, get_all_users,
    update_user, delete_user
)

def add_user(nome, idade, genero, email, senha):
    return create_user(nome, idade, genero, email, senha)

def get_user(user_id):
    return get_user_by_id(user_id)

def get_users():
    return get_all_users()

def edit_user(user_id, nome, idade, email):
    update_user(user_id, nome, idade, email)

def remove_user(user_id):
    delete_user(user_id)