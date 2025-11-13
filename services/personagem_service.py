from dao.personagem_dao import (
    create_personagem, get_personagem_by_id, get_all_personagens,
    update_personagem, delete_personagem
)

def add_personagem(usuario_id, sapato, acessorios, roupa, cabelo, corpo):
    return create_personagem(usuario_id, sapato, acessorios, roupa, cabelo, corpo)

def get_personagem(personagem_id):
    return get_personagem_by_id(personagem_id)

def get_personagens():
    return get_all_personagens()

def edit_personagem(personagem_id, sapato, acessorios, roupa, cabelo, corpo):
    update_personagem(personagem_id, sapato, acessorios, roupa, cabelo, corpo)

def remove_personagem(personagem_id):
    delete_personagem(personagem_id)
