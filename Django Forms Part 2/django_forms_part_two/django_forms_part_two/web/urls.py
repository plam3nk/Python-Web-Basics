from django.urls import path

from django_forms_part_two.web.views import index

urlpatterns = [
    path('', index, name='index'),
]