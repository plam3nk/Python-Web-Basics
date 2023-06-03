from django.db import models


# Create your models here.

class EmployeeProject(models.Model):
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=60)


class Employee(models.Model):
    LEVEL_JUNIOR = 'jur'
    LEVEL_MIDDLE = 'mid'
    LEVEL_SENIOR = 'sen'
    LEVEL_CHOICES = (
        (LEVEL_JUNIOR, 'Junior'),
        (LEVEL_MIDDLE, 'Middle'),
        (LEVEL_SENIOR, 'Senior'),
    )

    # CASCADE (Department + all connected employees)
    # RESTRICT (if department has employees, stop deletion prevent Employees deletion)
    # SET_NULL (set null if it is optional)

    department = models.ForeignKey(to=Department, on_delete=models.RESTRICT, null=True)

    project = models.ManyToManyField(Project)

    # Varying char (30) | or | VARCHAR (30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    description = models.TextField()

    age = models.IntegerField()  # positive and negative1
    experience = models.PositiveIntegerField()

    birth_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)  # only created time
    updated_on = models.DateTimeField(auto_now=True)  # each time update

    is_manager = models.BooleanField(default=None)

    #  profile_link = models.URLField()

    email = models.EmailField()

    # junior, middle, senior

    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

    # define structure into DB
    # gets data from DB (instances)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.full_name}"


class Profile(models.Model):
    DESK_ONE = 'one'
    DESK_TWO = 'two'
    DESK_CHOICES = (
        (DESK_ONE, 'desk 1'),
        (DESK_TWO, 'desk 2'),
    )
    desk = models.CharField(choices=DESK_CHOICES)

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
