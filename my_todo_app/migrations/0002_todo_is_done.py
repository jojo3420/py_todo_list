# Generated by Django 2.2.1 on 2021-08-18 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
