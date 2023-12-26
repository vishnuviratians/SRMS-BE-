from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    date_of_joining = models.DateField()
    date_of_birth = models.DateField()
    dept = models.ForeignKey('Department', on_delete=models.CASCADE)    
    status = models.CharField(max_length=10)  # Assuming 'Active' or 'Inactive'
    blood_group = models.CharField(max_length=4)
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Student'  


class Department(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = 'Department' 


    

    # Add more fields as per your table structure
class User(models.Model):
        email = models.CharField(max_length=255,unique=True)
        password = models.CharField(max_length=20)

        

        class Meta:
            db_table = 'User' 