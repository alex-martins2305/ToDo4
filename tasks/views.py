from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import date, datetime
from .models import Task
from .forms import newTaskForm, newTaskForm2
from .staff_functions import *

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

        titulo="Dashboard"

        if request.user.is_superuser:  
            choices=create_choices()
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                Tasks_atrasadasTodas=tasks_atrasadas_by_user(name)
                TasksDoDiaTodas=tasks_dodia_by_user(name)
                Tasks_futurasTodas=tasks_futuras_by_user(name)           
            else:
                print('bosta')
                Tasks_atrasadasTodas=func_all_atrasadas()
                TasksDoDiaTodas=func_all_dodia()
                Tasks_futurasTodas=func_all_futuras()

            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadasTodas, 'TasksDoDia':TasksDoDiaTodas, 'Tasks_futuras':Tasks_futurasTodas, 'dashboards': titulo, 'usuarios':choices} )
        else:
            Tasks_atrasadas=atrasadas_by_user_notInit_Init(name_logado)
            TasksDoDia=dodia_by_user_notInit_Init(name_logado) 
            Tasks_futuras=futuras_by_user_notInit_Init(name_logado)

            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadas, 'TasksDoDia':TasksDoDia, 'Tasks_futuras':Tasks_futuras, 'dashboards': titulo} )
    else:
        return redirect ('login')

def tasksAtrasadas(request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

        titulo="Tarefas Atrasadas"

        choices=create_choices()
            
        if request.user.is_superuser:
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                tasks_atrasadas_by_user(name)
            else:
                Tasks_atrasadasTodas=all_atrasadas_iniciada_naoIniciada()
           
            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadasTodas, 'atrasadas': titulo,'usuarios':choices } )
        else:
            Tasks_atrasadas=atrasadas_by_user_notInit_Init(name_logado)
            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadas,'atrasadas': titulo} )
    else:
        return redirect ('login')
    
def tasksDoDia(request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

        titulo="Tarefas do dia"

        choices=create_choices()
            
        if request.user.is_superuser:
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                TasksDoDiaTodas=tasks_dodia_by_user(name)
            else: 
                TasksDoDiaTodas=all_dodia_iniciada_naoIniciada()
           
            return render(request, 'tasks/dashboard.html', {'TasksDoDia':TasksDoDiaTodas, 'dodia': titulo,'usuarios':choices } )
        else:
            TasksDoDia=dodia_by_user_notInit_Init(name_logado)
            return render(request, 'tasks/dashboard.html', {'TasksDoDia':TasksDoDia,'dodia': titulo} )
    else:
        return redirect ('login')
        
def tasksFuturas(request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

        titulo="Tarefas futuras"

        choices=create_choices()
            
        if request.user.is_superuser:
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                Tasks_futurasTodas=tasks_futuras_by_user(name)
            else:
                Tasks_futurasTodas=all_futuras_iniciada_naoIniciada()
           
            return render(request, 'tasks/dashboard.html', {'Tasks_futuras':Tasks_futurasTodas, 'futuras': titulo,'usuarios':choices } )
        else:
            Tasks_futuras=futuras_by_user_notInit_Init(name_logado)
            return render(request, 'tasks/dashboard.html', {'Tasks_futuras':Tasks_futuras,'futuras': titulo} )
    else:
        return redirect ('login')

    
def tasksFinalizadas(request):

    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

        titulo="Tarefas finalizadas"

        choices=create_choices()
            
        if request.user.is_superuser:
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                Tasks_finalizadasTodas=finalizadas_by_user(name)
            else:
                Tasks_finalizadasTodas=all_finalizadas()
           
            return render(request, 'tasks/dashboard.html', {'Tasks_finalizadas':Tasks_finalizadasTodas, 'finalizadas': titulo,'usuarios':choices } )
        else:
            Tasks_finalizadas=finalizadas_by_user(name_logado)
            return render(request, 'tasks/dashboard.html', {'Tasks_finalizadas':Tasks_finalizadas,'finalizadas': titulo} )
    else:
        return redirect ('login')
    
def tasksJustificadas(request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

        titulo="Tarefas justificadas"

        choices=create_choices()
            
        if request.user.is_superuser:
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                Tasks_justificadasTodas=justificadas_by_user(name)
            else:
                Tasks_justificadasTodas=all_justificadas()
           
            return render(request, 'tasks/dashboard.html', {'Tasks_justificadas':Tasks_justificadasTodas, 'justificadas': titulo,'usuarios':choices } )
        else:
            Tasks_justificadas=justificadas_by_user(name_logado)
            return render(request, 'tasks/dashboard.html', {'Tasks_justificadas':Tasks_justificadas,'justificadas': titulo} )
    else:
        return redirect ('login')
    
def tasksTodas(request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

        titulo="Todas as tarefas"

        Tasks_atrasadasTodas=func_all_atrasadas()
        Tasks_atrasadas=tasks_atrasadas_by_user(name_logado) 

        TasksDoDiaTodas=func_all_dodia()
        TasksDoDia=tasks_dodia_by_user(name_logado)
        
        Tasks_futurasTodas=func_all_futuras()
        Tasks_futuras=tasks_futuras_by_user(name_logado)

        User = get_user_model()
        users = User.objects.all()
        choices=[]
        for user in users:
            list_element=(user.username, user.username)
            choices.append(list_element)

        if request.user.is_superuser:
            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadasTodas, 'TasksDoDia':TasksDoDiaTodas, 'Tasks_futuras':Tasks_futurasTodas, 'dashboards': titulo} )
        else:
            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadas, 'TasksDoDia':TasksDoDia, 'Tasks_futuras':Tasks_futuras, 'dashboards': titulo} )

    else:
        return redirect ('login')
    
def tasks(request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username
        Tasks_futuras=futuras_by_user_notInit_Init(name_logado)
    else:
        return redirect ('login')
    
def taskview(request,task_id):
    task_clicada=get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_clicada.html', {'task':task_clicada})

def initTask(request):
    if request.method == 'POST':
        taskId=request.POST['task_id']
    task_clicada=get_object_or_404(Task, pk=taskId)  
    task_clicada.etapas='iniciada'
    task_clicada.start_at=date.today()
    task_clicada.save()
    return render(request, 'tasks/task_clicada.html', {'task':task_clicada})

def finishTask(request):  
    if request.method == 'POST':
        taskId=request.POST['task_id']
    task_clicada=get_object_or_404(Task, pk=taskId)  
    task_clicada.etapas='finalizada'
    task_clicada.finished_at=date.today()
    task_clicada.save()
    return render(request, 'tasks/task_clicada.html', {'task':task_clicada})

def saveTaskObs(request):
    if request.method == 'POST':
        taskId=request.POST['task_id']
        obsText=request.POST['obsText']
    task_clicada=get_object_or_404(Task, pk=taskId)  
    task_clicada.obs=obsText
    if task_clicada.etapas=='quase_justificada':
        task_clicada.etapas='justificada'
    task_clicada.save()
    return render(request, 'tasks/task_clicada.html', {'task':task_clicada})

def JustificyTask(request):
    if request.method == 'POST':
        taskId=request.POST['task_id']
    task_clicada=get_object_or_404(Task, pk=taskId)
    if task_clicada.obs=="":
        task_clicada.etapas='quase_justificada'
    else:
        task_clicada.etapas='justificada'
        task_clicada.update_at=date.today()
    task_clicada.save()
    return render(request, 'tasks/task_clicada.html', {'task':task_clicada})

def newTask(request):
    if request.user.is_superuser:
        form = newTaskForm(request.POST or None)
    else:
        form =newTaskForm2(request.POST or None)
    if form.is_valid():
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        need_init_at = request.POST.get('need_init_at')
        pessoa = request.POST.get('pessoa')

        # Caso a sua data não esteja em formato Date, será necessário fazer a conversão
        datetime_obj = datetime.strptime(need_init_at, '%d/%m/%Y')
        # Uma vez convertida a data ficará no formato padrão 2017-12-29 00:00:00

        if request.user.is_superuser:
            user = get_object_or_404(User, username=pessoa)
        else:
            user = get_object_or_404(User, pk=request.user.id)

        nome_pessoa=user.username
        
        if Task.objects.filter(titulo=titulo, need_init_at=datetime_obj, pessoa=user).exists():
            messages.error(request, 'Já existe uma tarefa para esse usuário com mesmo título e mesma data.')
            return render(request, "tasks/newtask.html", {'form':form})
        else:
            task=Task.objects.create(pessoa=user, nome_pessoa=nome_pessoa, titulo=titulo, descricao=descricao, need_init_at=datetime_obj)
            task.save()
        #print(titulo, " ", descricao, "  ", need_init_at, " ", datetime_obj)
        #task=Task.objects.create(pessoa= user, tituto=titulo, descricao=descricao, need_init_at=need_init_at)   
        return redirect ('dashboard')
    else:
        return render(request, "tasks/newtask.html", {'form':form})

def search (request):
    if request.user.is_authenticated:
        id = request.user.id
        name_logado=request.user.username

    if request.user.is_superuser:
        all_atrasadas=func_all_atrasadas()
        all_dodia=func_all_dodia()
        all_futuras=func_all_futuras()
        print('SuperUser selecionada todoas tarefas')
    else:
        all_atrasadas=tasks_atrasadas_by_user(name_logado)
        all_dodia = tasks_dodia_by_user(name_logado)
        all_futuras=tasks_futuras_by_user(name_logado)

    name_to_search = request.POST['input_search'].lower()

    if name_to_search:
        search_in_atrasadas=all_atrasadas.filter(titulo__icontains=name_to_search)|all_atrasadas.filter(descricao__icontains=name_to_search)|all_atrasadas.filter(titulo__icontains=name_to_search.capitalize())|all_atrasadas.filter(descricao__icontains=name_to_search.capitalize())|all_atrasadas.filter(titulo__icontains=name_to_search.upper())|all_atrasadas.filter(descricao__icontains=name_to_search.upper())

        search_in_doDia=all_dodia.filter(titulo__icontains=name_to_search)|all_dodia.filter(descricao__icontains=name_to_search)|all_dodia.filter(titulo__icontains=name_to_search.capitalize())|all_dodia.filter(descricao__icontains=name_to_search.capitalize())|all_dodia.filter(titulo__icontains=name_to_search.upper())|all_dodia.filter(descricao__icontains=name_to_search.upper())

        search_in_futuras=all_futuras.filter(titulo__icontains=name_to_search)|all_futuras.filter(descricao__icontains=name_to_search)|all_futuras.filter(titulo__icontains=name_to_search.capitalize())|all_futuras.filter(descricao__icontains=name_to_search.capitalize())|all_futuras.filter(titulo__icontains=name_to_search.upper())|all_futuras.filter(descricao__icontains=name_to_search.upper())

        titulo="Busca de tarefas que contém "+name_to_search.upper()+":"

        Tasks_atrasadas=search_in_atrasadas

        TasksDoDia=search_in_doDia
    
        Tasks_futuras=search_in_futuras
    else:
        titulo="Sua busca por "+name_to_search+" não encontrou resultados."
        Tasks_atrasadas=""
        TasksDoDia=""
        Tasks_futuras=""

    return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadas, 'TasksDoDia':TasksDoDia, 'Tasks_futuras':Tasks_futuras, 'search': titulo} )

def teste(request):
    return render(request, 'teste.html')