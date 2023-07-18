from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    STATUS=(
        ("atrasada", "Atrasada"),
        ("no dia", "No Dia"),
        ("futura", "Futura"),
    )
    ETAPA=(
        ('não iniciada', 'não iniciada'),
        ('iniciada','iniciada'),
        ('finalizada', 'finalizada'),
        ('justificada','justificada'),
    )
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=255)
    descricao=models.TextField()
    status=models.CharField(
        max_length=13,
        choices=STATUS, 
        blank=True
        )
    etapas=models.CharField(
        max_length=13,
        choices=ETAPA, 
        default='não iniciada'
        )
    created_at=models.DateField(auto_now_add=True)
    need_init_at=models.DateField(default='01/01/2023')
    started=models.BooleanField(default=False)
    start_at=models.DateField(null=True, blank=True)
    finished=models.BooleanField(default=False)
    finished_at=models.DateField(null=True, blank=True)
    update_at=models.DateField(null=True, blank=True)
    obs=models.TextField(blank=True)
    postponed=models.BooleanField(default=False)
    postponed_at=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo