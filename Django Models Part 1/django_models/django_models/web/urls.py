from django.urls import path

from django_models.web import views

urlpatterns = [
    path('', views.index, name='index')
]