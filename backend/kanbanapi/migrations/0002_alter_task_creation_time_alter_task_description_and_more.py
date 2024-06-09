# Generated by Django 5.0.6 on 2024-06-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanbanapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_by',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='finish_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Черновик'), (1, 'В Очереди'), (2, 'Выполняется'), (3, 'Срочно'), (4, 'Выполнена')], default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='work_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]