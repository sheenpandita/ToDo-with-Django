from asyncio import all_tasks
from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
       #Handle the form
       title = request.POST['title']
       desc = request.POST['desc']
       print(title,desc)
       ins = Task(taskTitle=title, taskDesc=desc)
       ins.save()
       context = {'success': True}

    
    return render(request, 'index.html', context)

def tasks(request):
    all_tasks = Task.objects.all()
    context = {'tasks': all_tasks}
    return render(request, 'task.html', context)

