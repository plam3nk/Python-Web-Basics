from django.urls import path

from django_templates.examples import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_view, name='contact page'),
    path('about/', views.about_view, name='about page')
]