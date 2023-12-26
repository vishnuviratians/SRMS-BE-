# serializers.py
from rest_framework import serializers
from .models import Department, Student, User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'Password']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = 'id',
        'name',
        'age',
        'grade',
        'phone_no',
        'address',
        'Date_of_Joining',
        'Date_of_Birth',
        'dept_id',
        'status',
        'blood_group',
        'created_at',
        'modified_at'  # You can specify specific fields here if needed





