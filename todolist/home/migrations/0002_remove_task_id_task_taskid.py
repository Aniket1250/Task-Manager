# Generated by Django 4.2.7 on 2023-11-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='taskid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]