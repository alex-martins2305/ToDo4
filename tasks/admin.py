from django.contrib import admin
from .models import Task

class ListandoTasks(admin.ModelAdmin):
    list_display =('id', 'titulo', 'etapas', 'need_init_at')
    list_display_links=('id','etapas' )
    search_fields=('titulo',)
    list_filter=('pessoa',)
    list_per_page=20

admin.site.register(Task, ListandoTasks)