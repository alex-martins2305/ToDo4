from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
users = User.objects.all()
from datetime import date, datetime
from .models import Task
from .forms import newTaskForm, newTaskForm2


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id

        titulo="Dashboard"

        if request.user.is_superuser:  
            choices=create_choices()
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                Tasks_atrasadasTodas=Task.objects.filter(need_init_at__lt=date.today(),nome_pessoa=name).values().order_by('-created_at') 
                TasksDoDiaTodas=Task.objects.filter(need_init_at__exact=date.today(), nome_pessoa=name).values().order_by('-created_at')
                Tasks_futurasTodas=Task.objects.filter(need_init_at__gt=date.today(), nome_pessoa=name).values().order_by('-created_at')
            else:
                print('bosta')
                Tasks_atrasadasTodas=Task.objects.filter(need_init_at__lt=date.today()).values().order_by('-created_at') 
                TasksDoDiaTodas=Task.objects.filter(need_init_at__exact=date.today()).values().order_by('-created_at')
                Tasks_futurasTodas=Task.objects.filter(need_init_at__gt=date.today()).values().order_by('-created_at')

            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadasTodas, 'TasksDoDia':TasksDoDiaTodas, 'Tasks_futuras':Tasks_futurasTodas, 'dashboards': titulo, 'usuarios':choices} )
        else:
            Tasks_atrasadas1=Task.objects.filter(need_init_at__lt=date.today(), pessoa=id).values().order_by('-created_at') 
            Tasks_atrasadas=Tasks_atrasadas1.filter(etapas='não iniciada')|Tasks_atrasadas1.filter(etapas='iniciada')

            TasksDoDia1=Task.objects.filter(need_init_at__exact=date.today(), pessoa=id ).values().order_by('-created_at')
            TasksDoDia=TasksDoDia1.filter(etapas='iniciada')|TasksDoDia1.filter(etapas='não iniciada')
            
            Tasks_futuras1=Task.objects.filter(need_init_at__gt=date.today(), pessoa=id ).values().order_by('-created_at')
            Tasks_futuras=Tasks_futuras1.filter(etapas='não iniciada')|Tasks_futuras1.filter(etapas='iniciada')

            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadas, 'TasksDoDia':TasksDoDia, 'Tasks_futuras':Tasks_futuras, 'dashboards': titulo} )
    else:
        return redirect ('login')

def tasksAtrasadas(request):
    if request.user.is_authenticated:
        id = request.user.id

        titulo="Tarefas Atrasadas"

        choices=create_choices()
            
        if request.user.is_superuser:
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                Tasks_atrasadasTodas=Task.objects.filter(need_init_at__lt=date.today(), nome_pessoa=name).values().order_by('-created_at')
            else:
                Tasks_atrasadas1=Task.objects.filter(need_init_at__lt=date.today()).values().order_by('-created_at') 
                Tasks_atrasadasTodas=Tasks_atrasadas1.filter(etapas='não iniciada')|Tasks_atrasadas1.filter(etapas='iniciada')
           
            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadasTodas, 'atrasadas': titulo,'usuarios':choices } )
        else:
            Tasks_atrasadas1=Task.objects.filter(need_init_at__lt=date.today(), pessoa=id).values().order_by('-created_at') 
            Tasks_atrasadas=Tasks_atrasadas1.filter(etapas='não iniciada')|Tasks_atrasadas1.filter(etapas='iniciada')
            return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadas,'atrasadas': titulo} )
    else:
        return redirect ('login')
    
def tasksDoDia(request):
    if request.user.is_authenticated:
        id = request.user.id

        titulo="Tarefas do dia"

        choices=create_choices()
            
        if request.user.is_superuser:
            try:    
                name = request.POST['user']
            except:
                name=""
            if name!="":
                TasksDoDiaTodas=Task.objects.filter(need_init_at__exact=date.today(), nome_pessoa=name).values().order_by('-created_at')
            else:
                TasksDoDia1=Task.objects.filter(need_init_at__exact=date.today()).values().order_by('-created_at') 
                TasksDoDiaTodas=TasksDoDia1.filter(etapas='não iniciada')|TasksDoDia1.filter(etapas='iniciada')
           
            return render(request, 'tasks/dashboard.html', {'TasksDoDia':TasksDoDiaTodas, 'dodia': titulo,'usuarios':choices } )
        else:
            TasksDoDia1=Task.objects.filter(need_init_at__exact=date.today(), pessoa=id).values().order_by('-created_at') 
            TasksDoDia=TasksDoDia1.filter(etapas='não iniciada')|TasksDoDia1.filter(etapas='iniciada')
            return render(request, 'tasks/dashboard.html', {'TasksDoDia':TasksDoDia,'dodia': titulo} )
    else:
        return redirect ('login')
        
def tasksFuturas(request):
    if request.user.is_authenticated:
        id = request.user.id
        titulo="Tarefas Futuras"
        Tasks_futurasTodas=Task.objects.filter(need_init_at__gt=date.today(), pessoa=id ).values().order_by('-created_at')
        Tasks_futuras1=Task.objects.filter(need_init_at__gt=date.today(), pessoa=id ).values().order_by('-created_at')
        Tasks_futuras=Tasks_futuras1.filter(etapas='não iniciada')|Tasks_futuras1.filter(etapas='iniciada')
        if request.user.is_superuser:
            choices=create_choices()
            return render(request, 'tasks/dashboard.html', {'Tasks_futuras':Tasks_futurasTodas, 'futuras': titulo, 'usuarios':choices} )
        else:
            return render(request, 'tasks/dashboard.html', {'Tasks_futuras':Tasks_futuras,'futuras': titulo} )
    else:
        return redirect ('login')
    
def tasksFinalizadas(request):
    if request.user.is_authenticated:
        id = request.user.id
        titulo="Tarefas Finalizadas"
        Tasks_finalizadasTodas=Task.objects.filter(etapas='finalizada')
        Tasks_finalizadas=Task.objects.filter(etapas='finalizada', pessoa=id)
        if request.user.is_superuser:
            choices=create_choices()
            return render(request, 'tasks/dashboard.html', {'Tasks_finalizadas':Tasks_finalizadasTodas, 'finalizadas': titulo, 'usuarios':choices} )
        else:
            return render(request, 'tasks/dashboard.html', {'Tasks_finalizadas':Tasks_finalizadas, 'finalizadas': titulo} )
    else:
        return redirect ('login')
    
def tasksJustificadas(request):
    if request.user.is_authenticated:
        id = request.user.id
        titulo="Tarefas Justificadas"
        Tasks_justificadasTodas=Task.objects.filter(etapas='justificada', pessoa=id)
        Tasks_justificadas=Task.objects.filter(etapas='justificada', pessoa=id)
        print(Tasks_justificadas)
        if request.user.is_superuser:
            choices=create_choices()
            return render(request, 'tasks/dashboard.html', {'Tasks_justificadas':Tasks_justificadasTodas, 'justificadas': titulo, 'usuarios':choices} )
        else:
            return render(request, 'tasks/dashboard.html', {'Tasks_justificadas':Tasks_justificadas, 'justificadas': titulo} )
    else:
        return redirect ('login')
    
def tasksTodas(request):
    if request.user.is_authenticated:
        id = request.user.id
        titulo="Todas as tarefas"

        Tasks_atrasadasTodas=Task.objects.filter(need_init_at__lt=date.today()).values().order_by('-created_at') 
        Tasks_atrasadas=Task.objects.filter(need_init_at__lt=date.today(), pessoa=id).values().order_by('-created_at') 

        TasksDoDiaTodas=Task.objects.filter(need_init_at__exact=date.today()).values().order_by('-created_at')
        TasksDoDia=Task.objects.filter(need_init_at__exact=date.today(), pessoa=id ).values().order_by('-created_at')
        
        Tasks_futurasTodas=Task.objects.filter(need_init_at__gt=date.today()).values().order_by('-created_at')
        Tasks_futuras=Task.objects.filter(need_init_at__gt=date.today(), pessoa=id ).values().order_by('-created_at')

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
        Tasks_futuras1=Task.objects.filter(need_init_at__gt=date.today(), pessoa=id ).values().order_by('-created_at')
        Tasks_futuras=Tasks_futuras1.filter(etapas='não iniciada')|Tasks_futuras1.filter(etapas='iniciada')
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

def postponeTask(request):
    pass

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

def create_choices():
    User = get_user_model()
    users = User.objects.all()
    choices=[]
    for user in users:
        list_element=(user.username)
        choices.append(list_element)
    return (choices)

def teste(request):
    return render(request, 'teste.html')