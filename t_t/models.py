from django.db import models
from ckeditor.fields import RichTextField
from datetime import  datetime, date
class Table(models.Model):
    name = models.CharField('Table name', max_length=150, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):

    CHOISES = (
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Ready for test', 'Ready for test'),
        ('Closed', 'Closed'),

    )
    PRIORITY = (

        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),

    )

    table_name = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    subject = models.CharField("Task subject", max_length=250, null=True)
    status = models.CharField(max_length=200,default='To do', choices=CHOISES)
    task_title = models.CharField(max_length=400, null=True)
    images = models.ImageField(upload_to="gallery", null=True)
    description = RichTextField("Task description", null=True)
    priority = models.CharField(max_length=200, null=True, choices= PRIORITY)


    def __str__(self):
        return self.subject
