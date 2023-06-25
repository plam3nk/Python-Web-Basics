from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
def string_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


def first_char_is_letter(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 25
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_LAST_NAME = 35
    MIN_LEN_LAST_NAME = 1
    MAX_LEN_EMAIL = 40
    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 8

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            first_char_is_letter,
        )
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LEN_LAST_NAME),
            first_char_is_letter,
        )
    )

    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=(
            MinLengthValidator(MIN_LEN_PASSWORD),
        )
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=False,
        default=18
    )


class Fruit(models.Model):
    MIN_LEN_FRUIT = 2
    MAX_LEN_FRUIT = 30

    name = models.CharField(
        max_length=MAX_LEN_FRUIT,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LEN_FRUIT),
            string_only_letters,
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )
