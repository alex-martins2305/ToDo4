# Generated by Django 4.2.3 on 2023-07-16 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_finished_at_alter_task_postponed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='finished_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='postponed_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='update_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]