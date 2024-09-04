from django.shortcuts import render
from .models import Tasks 

def task_list(request):
    tasks = [
        {'title': 'Buy groceries', 'description': 'Milk, Bread, Eggs'},
        {'title': 'Study Django', 'description': 'Complete the task_list function'},
        {'title': 'Exercise', 'description': '30 minutes of running'}
    ]
    #tasks = Task.objects.all()
    return render(request, 'task_list.html',{'tasks':tasks})

