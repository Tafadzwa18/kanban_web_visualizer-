from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def kanban_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        # Create the new task using the data from the modal
        Task.objects.create(title=title, description=description, status=status)
        return redirect('kanban')

    tasks = Task.objects.all()
    return render(request, 'kanban.html', {'tasks': tasks})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})