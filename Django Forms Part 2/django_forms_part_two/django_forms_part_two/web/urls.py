from django.urls import path

from django_forms_part_two.web.views import index, create_person, list_persons

urlpatterns = [
    path('', index, name='index'),
    path('persons/', list_persons, name='list persons'),
    path('persons/create/', create_person, name='create person')
]

