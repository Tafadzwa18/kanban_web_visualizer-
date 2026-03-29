from django.shortcuts import get_object_or_404, redirect, render
from .models import *

# Create your views here.
def kanban_view(request):
    if request.method == "POST":
        action = request.POST.get('action')
        
        if action == "create":
            Task.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                status=request.POST.get('status')
            )
        
        elif action == "edit":
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            task.save()
            
        elif action == "delete":
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.delete()

        return redirect('kanban')

    tasks = Task.objects.all()
    return render(request, 'kanban.html', {'tasks': tasks})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})