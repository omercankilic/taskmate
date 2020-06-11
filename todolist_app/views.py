from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def delete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if(task.manage == request.user):
        task.delete()
    else:
        messages.error(request,("You dont have right to delete this task"))
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method =="POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request,("New Task Added Succesfully"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request,'edit.html',{'task_obj':task_obj})

@login_required
def complete_task(request,task_id):
    task = TaskList.objects.get(pk=task_id)
    if(task.done):
        if task.manage ==request.user:
            task.done=False
            task.save()
        else:
            messages.error(request,("Access denied to do that"))
    else:
        if task.manage== request.user:    
            task.done=True
            task.save()
        else:
            messages.error(request,("Access denied to do that"))
    return redirect('todolist')

#this means you can access this method only if  you are logged in
@login_required
def todolist(request):
    #This will help us fetch all objects
    if request.method =="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()       
        messages.success(request,("New Task Added Succesfully"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(manage=request.user)
        #pagination
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request,'todolist.html',{'all_tasks':all_tasks})

    """
    context = {
        'todolist_text':"Welcome To Todo List Page",
    }
    """

def contact(request):
    context = {
        'contact_text':"Welcome to Contact Page",
    }
    return render(request,'contact.html',context)


def about(request):
    context = {
        'about_text':"Welcome to About Page",
    }
    return render(request,'about.html',context)


def index(request):
    context = {
        'index_text':"Welcome to Index Page",
    }
    return render(request,'index.html',context)