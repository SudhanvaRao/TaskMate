from django.core import paginator
from django.db.models import manager
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todolist_app.models import tasklist
from todolist_app.form import Taskforms
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def todolist(request):
    if request.method == "POST":
        form = Taskforms(request.POST or None)
        if form.is_valid:
            form.save(commit=False).manager = request.user
            form.save()
        messages.success(request, ("New Task Added"))
        return redirect('todolist')
    else:
        all_tasks = tasklist.objects.filter(manager=request.user)
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        
        context = {
            'all_tasks':all_tasks,
        }
        return render(request, 'todolist.html',context)

def contact(request):
    context = {
        'welcome_text':'Welcome to Contact Us Page',
        
    }
    return render(request, 'contactus.html',context)

def aboutus(request):
    context = {
        'welcome_text':'Welcome to About-Us Page',
        
    }
    return render(request, 'aboutus.html',context)

def index(request):
    context = {
        'welcome_text':'Welcome to Home Page',
        
    }
    return render(request, 'index.html',context)

@login_required
def delete(request,id):
    task = tasklist.objects.get(pk=id)
    
    if request.user == task.manager:
        task.delete()
    else:
        messages.error(request, ("Acess Denied"))
    return redirect('todolist')

@login_required
def edit(request,id):
    if request.method == "POST":
        task_obj = tasklist.objects.get(pk=id)
        form = Taskforms(request.POST or None,instance=task_obj)
        if form.is_valid:
            form.save()
            messages.success(request, ("Task Edited"))
        
        return redirect('todolist')
    else:
        task_obj = tasklist.objects.get(pk=id)
        context = {
            'task_obj':task_obj,
        }
        return render(request, 'edit_task.html',context)
    
@login_required    
def done(request,id):
    task_obj = tasklist.objects.get(pk=id)
    if request.user == task_obj.manager:
        task_obj.done = True
        task_obj.save()
    
    else:
        messages.error(request, ("Acess Denied"))
    
    return redirect('todolist')

@login_required
def not_done(request,id):
    task_obj = tasklist.objects.get(pk=id)
    if request.user == task_obj.manager:
        task_obj.done = False
        task_obj.save()
    
    else:
        messages.error(request, ("Acess Denied"))
    
    return redirect('todolist')
