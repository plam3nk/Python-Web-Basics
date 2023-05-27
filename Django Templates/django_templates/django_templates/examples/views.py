import datetime
import random

from django.shortcuts import render, redirect


# Create your views here.

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


some_student = Student('Plamen', 20)


def index(request):
    context = {
        'title': 'Home',
        'random_int': random.random(),
        'nested': {
            'second_title': 'value'
        },
        'student_age': some_student.get_age(),
        'students': ['Plamen', 'Ivan', 'Victoria', 'Victoria' , 'Pesho'],
        'students_second': [],
        'now': datetime.datetime.now(),
        'numbers': [1,2,3,4,5,6,7],
        'students_obj': [
            Student('Ivan', 20),
            Student('Victoria', 18),
            Student('Pesho', 40),
        ],
        'logged_in': True,
    }
    # context['nested']['second_title']

    return render(request, 'examples/partials/index.html', context=context)


def contact_view(request):
    return redirect('index')


def about_view(request):
    return render(request, 'examples/partials/about.html')