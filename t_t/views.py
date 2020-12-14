from django.shortcuts import render, redirect
from .forms import *
from .models import *



def index(request):
    form = TableForm()

    output = Table.objects.all()
    task = Task.objects.all()
    table_count = Table.objects.all().count()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 't_t/index.html', {'output': output, 'task': task, 'form': form, 'table_count':table_count})


def get_tasks(request, id):
    table = Table.objects.get(id=id)

    form_status = TaskFormStatus()
    tasks = table.task_set.all()
    task_count = tasks.count()
    color = 'danger'
    to_do = tasks.filter(status="To do")
    in_progress = tasks.filter(status="In progress")
    ready_for_test = tasks.filter(status="Ready for test")
    closed = tasks.filter(status="Closed")



    context = {'to_do': to_do,
               'in_progress': in_progress,
               'ready_for_test': ready_for_test,
               'closed': closed,
               'color': color,
               'task_count': task_count,
               'table': table,
               'form_status' : form_status
               }

    return render(request, 't_t/detail.html', context)


def taskPage(request, id):

    task = Task.objects.get(id=id)

    context = {"task": task}

    return render(request, 't_t/task-page.html', context)


def createTable(request):
    form = TableForm()

    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}

    return render(request, 't_t/create_table.html', context)



def updateTable(request, id):

    table = Table.objects.get(id=id)


    form = TableForm(instance=table)

    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form' : form}

    return render(request, 't_t/create_table.html', context)



def deleteTable(request, id):
    table = Table.objects.get(id=id)

    if request.method == 'POST':
        table.delete()
        return redirect('/')

    context = {'item': table}

    return render(request, 't_t/delete.html', context)


def createTask(request, id):
    table = Table.objects.get(id=id)

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/' + str(table.id))

    context = {'form_task': form, 'table': table}

    return render(request, 't_t/create_task.html', context)


def updateTask(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    table = task.table_name
    table_id = task.table_name.id
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/' + str(table_id))

    context = {'form_task': form, 'table': table}
    return render(request, 't_t/create_task.html', context)


def changeTaskStatus(request, id):
    task = Task.objects.get(id=id)

    table_id = task.table_name.id

    form = TaskFormStatus(instance=task)

    if request.method == 'POST':
        form = TaskFormStatus(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/' + str(table_id))

    context = {'form' : form, 'table_id': table_id}

    return render(request, 't_t/change_status.html', context)


def deleteTask(request, id):
    task = Task.objects.get(id=id)

    table_id = task.table_name.id

    if request.method == 'POST':
        task.delete()
        return redirect('/' + str(table_id))

    context = {'item': task}

    return render(request, 't_t/delete.html', context)
