from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import createNewTask, createNewProject

# Create your views here.
def index(request):
    title = "welcome to jango course"
    return render(request, 'index.html',{
        'titulo': title
    })
#asi se crea un diccionario
def about(request):
    username = 'Miguelito'
    return render(request, 'about.html', {
        'nombre' : username
    })

def hello(request, username):
    print(username) 
    return HttpResponse("<h1>Hello %s</h1>" % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'proyectos' : projects
    })

def task(request):
    Tasks = Task.objects.all()
    return render(request, 'task/task.html',{
        'tareas': Tasks
    }) 
def create_task(request):
    if request.method == 'GET':
        return render(request, 'task/create_task.html', {
            'form': createNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'], 
            description=request.POST['description'], 
            project_id=2  
        )
        return redirect('/task/')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': createNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST["name"])
        print(project) 
        return redirect('/projects/')
