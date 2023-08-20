from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:task_id>/', views.taskview, name='taskview'),
    path('dashboard/init_task/', views.initTask, name='initTask'),
    path('dashboard/finish_task/', views.finishTask, name='finishTask'),
    path('dashboard/justify_task/', views.JustificyTask, name='justifyTask'),
    path('dashboard/save_task/', views.saveTaskObs, name='saveTaskObs'),
    path('dashboard/new_task/', views.newTask, name='newtask'),
    path('dashboard/task_atrasadas/', views.tasksAtrasadas, name='tasksAtrasadas'),
    path('dashboard/tasks_do_dia/', views.tasksDoDia, name='tasksDoDia'),
    path('dashboard/task_futuras/', views.tasksFuturas, name='tasksFuturas'),
    path('dashboard/task_finalizadas/', views.tasksFinalizadas, name='tasksFinalizadas'),
    path('dashboard/task_justificadas/', views.tasksJustificadas, name='tasksJustificadas'),
    path('dashboard/task_todas/', views.tasksTodas, name='tasksTodas'),
    path('dashboard/search/', views.search, name='search'),
    path('teste/', views.teste, name='teste'),
    path('compra/', views.compra, name='compra'),

]
