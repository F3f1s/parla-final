from dao.atividade_dao import (
    create_atividade, get_atividade_by_id, get_all_atividades,
    update_atividade, delete_atividade
)

def add_atividade(tentativas, dificuldade, horario, erros):
    return create_atividade(tentativas, dificuldade, horario, erros)

def get_atividade(atividade_id):
    return get_atividade_by_id(atividade_id)

def get_atividades():
    return get_all_atividades()

def edit_atividade(atividade_id, tentativas, dificuldade, horario, erros):
    update_atividade(atividade_id, tentativas, dificuldade, horario, erros)

def remove_atividade(atividade_id):
    delete_atividade(atividade_id)
