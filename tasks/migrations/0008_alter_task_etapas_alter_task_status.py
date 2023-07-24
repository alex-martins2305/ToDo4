# Generated by Django 4.2.3 on 2023-07-21 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='etapas',
            field=models.CharField(choices=[('não iniciada', 'não iniciada'), ('iniciada', 'iniciada'), ('finalizada', 'finalizada'), ('justificada', 'justificada'), ('quase_justificada', 'quase_justificada')], default='não iniciada', max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('atrasada', 'Atrasada'), ('no dia', 'No Dia'), ('futura', 'Futura')], max_length=13),
        ),
    ]