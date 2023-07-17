from django.contrib import admin    
from tasks.models import Task

admin.site.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "id",
        "status",
        "need_init_at",
        "start_at",
        "finished_at",
        "update_at",
    ]
    list_filter = ["titulo", "descricao", "need_init_at"]
    search_fields = ["titulo", "descricao"]