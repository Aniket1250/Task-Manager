# Generated by Django 4.2.7 on 2023-11-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_task_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]