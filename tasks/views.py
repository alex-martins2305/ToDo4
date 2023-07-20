from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from datetime import date
from .models import Task

def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id

        Tasks_atrasadas=Task.objects.filter(need_init_at__lt=date.today(), pessoa=id).values().order_by('-created_at') 
        #Tasks_atrasadas=Tasks_atrasadas1.filter(etapas='não iniciada')|Tasks_atrasadas1.filter(etapas='iniciada')

        TasksDoDia=Task.objects.filter(need_init_at__exact=date.today(), pessoa=id ).values().order_by('-created_at')
        #TasksDoDia=TasksDoDia1.filter(etapas='iniciada')|TasksDoDia1.filter(etapas='não iniciada')
        
        Tasks_futuras=Task.objects.filter(need_init_at__gt=date.today(), pessoa=id ).values().order_by('-created_at')
        #Tasks_futuras=Tasks_futuras1.filter(etapas='não iniciada')|Tasks_futuras1.filter(etapas='iniciada')

        return render(request, 'tasks/dashboard.html', {'Tasks_atrasadas':Tasks_atrasadas, 'TasksDoDia':TasksDoDia, 'Tasks_futuras':Tasks_futuras} )
    else:
        return redirect ('login')

def taskview(request,task_id):
    task_clicada=get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task_clicada.html', {'task':task_clicada})

def initFinishTask(request):
    if request.method == 'POST':
        taskId=request.POST['task_id']
        print(taskId)
    task_clicada=get_object_or_404(Task, pk=taskId)
    if task_clicada.etapas=='' or task_clicada.etapas=='não iniciada' or task_clicada.etapas=='adiada':
        task_clicada.etapas='iniciada'
        task_clicada.save()
        print(task_clicada.etapas,2)
    else:
        if task_clicada.etapas=='iniciada':
            task_clicada.etapas='finalizada'
            task_clicada.save()
    return render(request, 'tasks/task_clicada.html', {'task':task_clicada})
    

def saveTaskObs(resquest):
    pass

def JustificyTask(request):
    pass

def postponeTask(request):
    pass