# Generated by Django 5.0.6 on 2024-06-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_telegram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
