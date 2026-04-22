
# Kanban Task Management System

A web-based task management system built with Django that allows organizations to manage employee tasks using a Kanban-style workflow.

## Overview

This application provides a structured way to manage tasks across different stages of completion. It enables administrators to assign and monitor tasks, while employees can track their progress through an intuitive visual board.

The system is designed to simulate real-world task management workflows used in teams and organizations.

## Features

- Kanban board (To Do, In Progress, Done)
- Task assignment to employees
- Employee management (admin-controlled)
- Secure admin-only employee registration
- Task tracking by status
- Responsive user interface using Bootstrap

## Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite


## How to Run

1. Clone the repository  
2. Navigate to the project folder  
3. Run migrations:
   python manage.py migrate  
4. Start server:
   python manage.py runserver  

## Future Improvements

- Drag-and-drop task movement
- Task priorities and deadlines
- Real-time updates (WebSockets)
- Notifications (email or in-app)
- Role-based permissions