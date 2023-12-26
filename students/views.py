
from .models import Student,Department,User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
# views.py
from django.http import JsonResponse
@csrf_exempt
def login_user(request):
    try:
        if request.method == 'POST':
            # Get data from the POST request 
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.filter (email=email)
            print(user)
            if user:
                if password ==user[0].password :
                    return JsonResponse({
                        'status': 'true',
                        'message': 'Login Successful',
                    })
                else:
                    return JsonResponse({
                        'status': 'false',
                        'message': 'Invalid Password',
                    })
            else:
                # Authentication failed
                return JsonResponse({
                    'status': 'false',
                    'message': 'Invalid Email'
                })
        else:
            return JsonResponse({
                            'status':'false',
                            'message': 'something went wrong'
                })
    except Exception as f:
        return JsonResponse({            
                            'status':'false',
                            'message': str(f)
                })


@csrf_exempt
def get_student(request):
    try:
        if request.method == 'POST':
            students = Student.objects.all().values(
                'id',
                'name',
                'phone_no',
                'address',
                'date_of_joining',
                'date_of_birth',
                'dept_id',
                'status',
                'blood_group',
                'created_at',
                'modified_at'
            )

            # Convert the queryset to a list of dictionaries
            students_list = list(students)

            # Check if any records were found
            if students_list:
                return JsonResponse({
                    'status':'true',
                    'message':'Success',
                    'data': students_list
                })
            else:
                return JsonResponse({
                    'status':'false',
                    'message': 'No students found'
                })

        else:
            return JsonResponse({
                'status':'false',
                'message': 'Invalid request method'
                })
    except:
            return JsonResponse({
                'status':'false',
                'message': 'Invalid request method'
                })
@csrf_exempt
def add_student(request):
    try:
        if request.method == 'POST':
            # Get data from the POST request
            name = request.POST.get('name')
            phone_no = request.POST.get('phone_no')
            address = request.POST.get('address')
            date_of_joining = request.POST.get('date_of_joining')
            date_of_birth = request.POST.get('date_of_birth')
            department = request.POST.get('department')        
            status = request.POST.get('status')
            blood_group = request.POST.get('blood_group')
            created_at = request.POST.get('created_at')
            modified_at = request.POST.get('modified_at')

            student = Student(
                name=name,
                phone_no=phone_no,
                address=address,
                date_of_joining=date_of_joining,
                date_of_birth=date_of_birth,
                dept_id=department,  # Assuming dept_id is the foreign key field in Student model
                status=status,
                blood_group=blood_group,
                created_at=created_at,
                modified_at=modified_at
            )
            student.save()
            return JsonResponse({
                    'status':'true',
                    'message':'Student Added Sucessfully'
            })
        else:
            return JsonResponse({
                'status':'false',
                'message': 'Invalid request method'
            })
         
    except Exception as e:
        return JsonResponse({                    
            'status':'false',
            'message': str(e)
            })
    
@csrf_exempt
def update_student(request, student_id):
    try:
        if request.method == 'POST':
            # Fetch the existing student record by ID
            student = Student.objects.get(id=student_id)
            # Update fields based on the data received in the POST request
            name = request.POST.get('name')
            phone_no = request.POST.get('phone_no')
            address = request.POST.get('address')
            date_of_joining = request.POST.get('date_of_joining')
            date_of_birth = request.POST.get('date_of_birth')
            dept_id = request.POST.get('dept_id')
            status = request.POST.get('status')
            blood_group = request.POST.get('blood_group')
            created_at = request.POST.get('created_at')
            modified_at = request.POST.get('modified_at')

            # Update the fields if the data is provided in the request
            if name:
                student.name = name
            if phone_no:
                student.phone_no = phone_no
            if address:
                student.address = address
            if date_of_joining:
                student.date_of_joining = date_of_joining
            if date_of_birth:
                student.date_of_birth = date_of_birth
            if dept_id:
                student.dept_id = dept_id  
            if status:
                student.status = status
            if blood_group:
                student.blood_group = blood_group
            if created_at:
                student.created_at = created_at
            if modified_at:
                student.modified_at = modified_at

            # Save the updated student record
            student.save()
            return JsonResponse({
                    'status':'true',
                    'message':'Student Updated Sucessfully',
                })
        else:
            return JsonResponse({
                'status':'false',
                'message': 'Invalid request method'
                })
    except Exception as f:
            return JsonResponse({
                            'status':'false',
                            'message': str(f)
                })
@csrf_exempt
def delete_student(request, student_id):
    try:
        if request.method == 'POST':
            # Fetch the student record by ID and delete it
            student = Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({
                    'status':'true',
                    'message':'Student Deleted Sucessfully',
                })
                 
        else:
            return JsonResponse({
                            'status':'false',
                            'message': 'Invalid request method'
                })
    except Exception as f:
            return JsonResponse({
                            'status':'false',
                            'message': str(f)
                })


#department

@csrf_exempt
def get_department_data(request):
    try:
        if request.method == 'POST':
            departments = Department.objects.all().values('id', 'department_name')
            departments_list = list(departments)
            if departments_list:
                return JsonResponse({
                    'status':'true',
                    'message':'Success',
                    'data': departments_list
            })
           
        else:
            return JsonResponse({
                'status':'false',
                'message': 'Invalid request method' 
            })   
    except Exception as f:
        return JsonResponse({
                        'status':'false',
                        'message': str(f)
            })

@csrf_exempt
def add_departments(request):
    try:
        if request.method == 'POST':
            # Get data from the POST request
            department_name = request.POST.get('department_name')
            department = Department.objects.create(department_name=department_name)
            return JsonResponse({
                    'status':'true',
                    'message':'Department added Sucessfully',
                })
        else:
            return JsonResponse({
                            'status':'false',
                            'message': 'Department name not provided'
                })
    except Exception as f:
        return JsonResponse({            
                            'status':'false',
                            'message': str(f)
                })

@csrf_exempt
def update_department(request, department_id):
    try:
        if request.method == 'POST':
            # Update fields based on the data received in the POST request
            department = Department.objects.get(id=department_id)
            department_name = request.POST.get('department_name')
            if department_name:
                department.department_name = department_name
            department.save
            return JsonResponse({
                    'status':'true',
                    'message':'Department Updated Sucessfully',
                })
        else:
                return JsonResponse({
                'status':'false',
                'message': 'Invalid request method'
                })
    except Exception as f :
        return JsonResponse({
                        'status':'false',
                        'message': str(f)
                })

@csrf_exempt
def delete_department(request, department_id):
    try:
        department = Department.objects.get(id=department_id)
        if request.method == 'POST':
            # Delete the department record
            department.delete()
            return JsonResponse({
                    'status':'true',
                    'message':'Department Deleted Sucessfully',
                })
        else:
            return JsonResponse({
                            'status':'false',
                            'message': 'Invalid request method'
                })
    except Exception as f:
        return JsonResponse({
                        'status':'false',
                        'message': str(f)
                })

@csrf_exempt
def get_user_data(request):
    try:
        if request.method == 'POST':
            user = User.objects.all().values('email', 'Password')
            user = list(user)
            if user:
                return JsonResponse({
                    'status':'true',
                    'message':'Success',
                    'data':user
            })
        else:
            return JsonResponse({
                'status':'false',
                'message': 'Invalid request method' 
            })   
    except Exception as f:
        return JsonResponse({
                        'status':'false',
                        'message': str(f)
            })
