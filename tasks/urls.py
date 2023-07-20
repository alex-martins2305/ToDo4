from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/task/<int:task_id>', views.taskview, name='taskview'),
    path('dashboard/init_finish_task/', views.initFinishTask, name='initFinishTask'),
]
