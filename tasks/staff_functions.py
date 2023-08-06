from .models import Task
from datetime import date, datetime
from django.contrib.auth import get_user_model

def create_choices():
    User = get_user_model()
    users = User.objects.all()
    choices=[]
    for user in users:
        list_element=(user.username)
        choices.append(list_element)
    return (choices)

# Pesquisas
def all_tasks():
    all=Task.objects.all
    return (all)

def nao_iniciadas_or_iniciadas():
    nao_iniciadas_or_iniciadas=Task.objects.filter(etapas='não iniciada')|Task.objects.filter(etapas='iniciada')
    return (nao_iniciadas_or_iniciadas)

def tasks_by_user(username):
    tasks_by_user=Task.objects.filter(nome_pessoa=username)
    return (tasks_by_user)

def func_all_atrasadas():
    all_atrasadas=Task.objects.filter(need_init_at__lt=date.today()).values().order_by('-created_at')
    return all_atrasadas

def func_all_dodia():
    all_dodia=Task.objects.filter(need_init_at__exact=date.today()).values().order_by('-created_at')
    return all_dodia

def func_all_futuras():
    all_futuras=Task.objects.filter(need_init_at__gt=date.today()).values().order_by('-created_at')
    return all_futuras

def tasks_atrasadas_by_user(username):
    tasks_atrasadas_by_user=Task.objects.filter(nome_pessoa=username, need_init_at__lt=date.today()).values().order_by('-created_at')
    return (tasks_atrasadas_by_user)

def tasks_dodia_by_user(username):
    tasks_dodia_by_user=Task.objects.filter(nome_pessoa=username, need_init_at__exact=date.today()).values().order_by('-created_at')
    return (tasks_dodia_by_user)

def tasks_futuras_by_user(username):
    tasks_futuras_by_user=Task.objects.filter(nome_pessoa=username, need_init_at__gt=date.today()).values().order_by('-created_at')
    return (tasks_futuras_by_user)

def all_atrasadas_iniciada_naoIniciada():
    all_atrasadas_iniciada_naoIniciada=func_all_atrasadas().filter(etapas='não iniciada')|func_all_atrasadas().filter(etapas='iniciada')
    return all_atrasadas_iniciada_naoIniciada

def all_dodia_iniciada_naoIniciada():
    all_dodia_iniciada_naoIniciada=func_all_dodia().filter(etapas='não iniciada')|func_all_dodia().filter(etapas='iniciada')
    return all_dodia_iniciada_naoIniciada

def all_futuras_iniciada_naoIniciada():
    all_futuras_iniciada_naoIniciada=func_all_futuras().filter(etapas='não iniciada')|func_all_futuras  ().filter(etapas='iniciada')
    return all_futuras_iniciada_naoIniciada

def all_finalizadas():
    all_finalizadas=Task.objects.filter(etapas='finalizada')
    return all_finalizadas

def finalizadas_by_user(username):
    finalizadas_by_user=Task.objects.filter(etapas='finalizada', nome_pessoa=username)
    return finalizadas_by_user

def justificadas_by_user(username):
    justificadas_by_user=Task.objects.filter(etapas='justificada', nome_pessoa=username)
    return justificadas_by_user

def all_justificadas():
    all_justificadas=Task.objects.filter(etapas='justificada')
    return all_justificadas

def atrasadas_by_user_notInit_Init(username):
    Tasks_atrasadas1=tasks_atrasadas_by_user(username)
    atrasadas_by_user_notInit_Init=Tasks_atrasadas1.filter(etapas='não iniciada')|Tasks_atrasadas1.filter(etapas='iniciada')
    return atrasadas_by_user_notInit_Init

def dodia_by_user_notInit_Init(username):
    Tasks_dodia1=tasks_dodia_by_user(username)
    dodia_by_user_notInit_Init=Tasks_dodia1.filter(etapas='não iniciada')|Tasks_dodia1.filter(etapas='iniciada')
    return dodia_by_user_notInit_Init

def futuras_by_user_notInit_Init(username):
    Tasks_futuras1=tasks_futuras_by_user(username)
    futuras_by_user_notInit_Init=Tasks_futuras1.filter(etapas='não iniciada')|Tasks_futuras1.filter(etapas='iniciada')
    return futuras_by_user_notInit_Init
