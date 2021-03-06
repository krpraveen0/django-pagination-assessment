# Generated by Django 4.0.1 on 2022-01-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_around_employee_boundaries'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomePaginate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boundaries', models.IntegerField()),
                ('around', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='around',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='boundaries',
        ),
    ]
