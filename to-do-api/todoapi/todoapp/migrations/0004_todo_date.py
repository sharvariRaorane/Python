# Generated by Django 4.1.3 on 2022-12-02 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_remove_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateField(default=datetime.date(2022, 12, 2)),
        ),
    ]