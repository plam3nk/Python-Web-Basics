from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def validate_text(value):
    # if valid:
    # do nothing
    # else:
    # raise ValidationException()
    if '_' in value:
        raise ValidationError('"_" is invalid character for "text"!')


def validate_priority(value):
    if value < 1 or value > 10:
        raise ValidationError('Priority must be between 1 and 10!')


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
            validate_text,
        ),
    )

    is_done = forms.BooleanField(
        required=False,
    )

    priority = forms.IntegerField(
        validators=(
            # validate_priority
            MinValueValidator(1),
            MaxValueValidator(10)
        ),
    )
    # Auto complete

    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     pass
    #     # raise ValidationError('Error! Number must be between 1 and 10')
    #
    # def clean_is_done(self):
    #     pass


def index(request):
    if request.method == 'GET':
        form = TodoForm()
    else:
        form = TodoForm(request.POST)

        if form.is_valid():
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context=context)