# Generated by Django 4.0.1 on 2022-01-27 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_customepaginate_remove_employee_around_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomePaginate',
            new_name='CustomPaginate',
        ),
    ]
