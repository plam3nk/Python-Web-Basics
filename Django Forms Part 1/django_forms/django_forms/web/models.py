from django.db import models

# Create your models here.


class Pet(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )

    def __str__(self):
        return f'{self.name}'

class Person(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )

    age = models.PositiveIntegerField()

    pets = models.ManyToManyField(
        Pet,
    )
