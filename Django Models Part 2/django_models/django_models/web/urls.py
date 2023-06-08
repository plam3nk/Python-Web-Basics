from django.urls import path

from django_models.web import views
from django_models.web.views import delete_employee

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
]