from django.contrib import admin
from .models import Employee, Department, Project, Profile


# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name', 'age', 'department']
    list_filter = ['level']
    search_fields = ('first_name', 'last_name', 'email')
    # fields = [('first_name', 'last_name'), 'email', 'age']
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('HR STUFF', {'fields': ('is_manager', 'email', 'level')})
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
