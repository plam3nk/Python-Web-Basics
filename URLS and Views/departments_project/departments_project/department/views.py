from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    print(request)
    return HttpResponse('index')


def details(request, department_id):
    department_map = {
        '1': "Python",
        '2': "C++",
        '3': "Java",
    }

    payload = f"Department: {department_map.get(str(department_id), 'Unknown')}"

    # return HttpResponse(payload)
    # return redirect('/departments/template/', department_id=department_id)
    # return redirect('https://google.bg/')

    return redirect('departments template', department_id=department_id)


def details_template(request, department_id):
    department_map = {
        '1': "Python",
        '2': "C++",
        '3': "Java",
    }

    payload = f"Department: {department_map.get(str(department_id), 'Unknown')}"

    context = {
        'title': 'Departments title from context',
        'payload': payload,
        # 'task': Department.objects.filter(department_id=department_id)
    }

    return render(request, 'departments/details.html', context=context)


def details_error(request, department_id):
    return HttpResponse('index')


