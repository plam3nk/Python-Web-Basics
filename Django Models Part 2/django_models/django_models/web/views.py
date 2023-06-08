from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department
# Create your views here.

from django.contrib.auth.models import User


def index(request):
    # lazy loading (it is not executed until is used)

    employees = Employee.objects.all()
    # employees2 = Employee.objects.filter(department_id=1)\
    employees2 = Employee.objects\
        .filter(department__name='IT')\
        # .order_by('first_name')

        # .filter(age__gte=20).\

    # 'department__name' in 'filter' is same as 'department.name'

    # 'get' returns an object, not QuerySet
    # 'get' returns a single object and throw error when multiple results or none
    # 'get' not lazy

    # get_object_or_404(Employee, level=Employee.LEVEL_SENIOR)

    department = Department.objects.get(pk=1)
    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    # departments = Department.objects.all()
    # employees2 = list(Employee.objects.all())
    # print(employees2)
    # print(employees)

    return render(request, 'web/index.html', context)


def delete_employee(request, pk):
    department_pk = 1
    # When 'Restricted' this must be done explicitly
    # When 'Cascade' this is done implicitly
    # Employee.objects.filter(department_id=department_pk)\
    #     .delete()
    # get_object_or_404(Department, pk=department_pk)\
    #     .delete()
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')
