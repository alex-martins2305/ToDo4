# Generated by Django 4.2.3 on 2023-07-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_finished_at_alter_task_postponed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='postponed_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='update_at',
            field=models.DateField(null=True),
        ),
    ]
