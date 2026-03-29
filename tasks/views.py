from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.db.models import Count, Q

def kanban_view(request):
    if request.method == "POST":
        action = request.POST.get('action')
        emp_id = request.POST.get('assigned_to')
        
        # Get the employee object if an ID was provided
        # Added a check to prevent errors if an invalid ID is sent
        employee = None
        if emp_id and emp_id.isdigit():
            employee = Employee.objects.filter(id=emp_id).first()

        if action == "create":
            Task.objects.create(
                title=request.POST.get('title'),
                description=request.POST.get('description'),
                status=request.POST.get('status'),
                assigned_to=employee
            )
        elif action == "edit":
            task = get_object_or_404(Task, id=request.POST.get('task_id'))
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            task.assigned_to = employee
            task.save()
        
        elif action == "delete":
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.delete()

        return redirect('kanban')
    
    # Filter Logic
    emp_filter = request.GET.get('employee')
    tasks = Task.objects.all()

    if emp_filter and emp_filter.isdigit():
        tasks = tasks.filter(assigned_to__id=emp_filter)    

    context = {
        'tasks': tasks,
        'employees': Employee.objects.all(),
        # Convert to int so the template {% if current_filter == emp.id %} works
        'current_filter': int(emp_filter) if emp_filter and emp_filter.isdigit() else None
    }
    return render(request, 'kanban.html', context)


def employee_list(request):
    # This logic is perfect for a performance-oriented dashboard
    employees = Employee.objects.annotate(
        active_tasks_count=Count('tasks', filter=~Q(tasks__status='done')),
        completed_tasks_count=Count('tasks', filter=Q(tasks__status='done'))
    )
    return render(request, 'employee_list.html', {'employees': employees})