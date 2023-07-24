from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/task/<int:task_id>', views.taskview, name='taskview'),
    path('dashboard/init_task/', views.initTask, name='initTask'),
    path('dashboard/finish_task/', views.finishTask, name='finishTask'),
    path('dashboard/justify_task/', views.JustificyTask, name='justifyTask'),
    path('dashboard/save_task/', views.saveTaskObs, name='saveTaskObs'),
    
]
