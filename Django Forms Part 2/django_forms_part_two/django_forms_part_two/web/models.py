from django.db import models

from django_forms_part_two.web.validators import validate_text, ValueInRangeValidator


# Create your models here.

class Person(models.Model):
    MAX_LENGTH_NAME = 20
    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
    )

    profile_image = models.ImageField(  # or FileField - for all files.
        upload_to='persons',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class Todo(models.Model):
    MAX_TODO_CONT_PER_PERSON = 3
    MAX_LENGTH_TEXT = 30
    text = models.CharField(
        max_length=MAX_LENGTH_TEXT,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    assigned = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )