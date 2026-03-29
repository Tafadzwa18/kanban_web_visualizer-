from django.urls import path
from tasks.views import *

urlpatterns = [
    path('', kanban_view, name='kanban'),
    path('employees/', employee_list, name='employee_list'),
]
