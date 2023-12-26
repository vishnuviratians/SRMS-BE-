# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('get_student/', views.get_student, name='get_student'),
    path('add_student/', views.add_student, name='add_student'),    
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    # Add more URL patterns as needed
    path('get_departments/', views.get_department_data, name='get_departments'), 
    path('add_departments/', views.add_departments, name='add_departments'), 
    path('update_departments/<int:department_id>/', views.update_department, name='update_departments'), 
    path('delete_departments/<int:department_id>/', views.delete_department, name='delete_department'),

    path('login/', views.login_user, name='login'), 
    path('get_user/', views.get_user_data, name='get_user'), 

]
