from django.forms import ModelForm
from .models import *

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['name']



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['table_name','subject','task_title','description', 'priority']


class TaskFormStatus(ModelForm):
    class Meta:
        model = Task
        fields = ['status']