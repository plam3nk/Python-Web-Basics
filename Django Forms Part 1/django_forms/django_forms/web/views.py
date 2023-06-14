from django import forms
from django.shortcuts import render

from django_forms.web.forms import PersonForm
from django_forms.web.models import Person


# Create your views here.


def index(request):
    name = None

    if request.method == 'GET':
        form = PersonForm()
    else:  # request.method == 'post'
        form = PersonForm(request.POST)
        form.is_valid()
        if form.is_valid():
            # 'is_valid()':
            # - validates the form, returns 'True' or 'False'
            # - Fills 'cleaned_data'
            name = form.cleaned_data['your_name']
            Person.objects.create(
                name=name,
            )
        else:
            pass
    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'index.html', context=context)


class PersonCreateForm(forms.ModelForm):
    # story = forms.CharField(
    #     widget=forms.Textarea(),
    # )

    class Meta:
        model = Person
        # fields - show only mentioned
        fields = '__all__'  # or ('name', 'age')
        # exclude - show everything except this
        # exclude = 'pets'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                },
            )
        }

    help_texts = {
        'name': 'Your name',
    }

    labels = {
        'age': 'Your age',
    }


def index_model_form(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()  # same as below
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            # person.pets.set(pets)
            # person.save()
            # print(form.cleaned_data)

    context = {
        'form': form,
    }
    return render(request, 'models_forms.html', context=context)
