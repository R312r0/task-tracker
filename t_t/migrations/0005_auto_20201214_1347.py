# Generated by Django 3.1.4 on 2020-12-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_t', '0004_remove_table_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('To do', 'To do'), ('In progress', 'In progress'), ('Ready for test', 'Ready for test'), ('Closed', 'Closed')], max_length=200, null='To do'),
        ),
    ]