from django.shortcuts import render

# Create your views here.

# register_user, login_user, show_profile_details, edit_profile, delete_profile


def register_user(request):
    return render(request, template_name='accounts/register-page.html')


def login_user(request):
    return render(request, template_name='accounts/login-page.html')


def show_profile_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
