from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.get_tasks, name='detail'),
    path('task_page/<int:id>', views.taskPage, name='task-page'),
    path('create_task/<int:id>', views.createTask, name='create_task'),
    path('create_table', views.createTable, name='create_table'),
    path('update_table/<int:id>', views.updateTable, name='update_table'),
    path('update_task/<int:id>', views.updateTask, name='update_task'),
    path('delete_table/<int:id>', views.deleteTable, name='delete_table'),
    path('delete_task/<int:id>', views.deleteTask, name='delete_task'),
    path('change_status/<int:id>', views.changeTaskStatus, name='change_status')
]
