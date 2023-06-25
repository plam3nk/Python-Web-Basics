from django.shortcuts import render, redirect

from fruitipedia.web.forms import ProfileCreateForm, FruitCreateForm, FruitEditForm, FruitDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from fruitipedia.web.models import Profile, Fruit


# Create your views here.

def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return redirect('profile_create')

    context = {
        'profile': profile
    }

    return render(request, template_name='core/index.html', context=context)


def dashboard(request):
    profile = get_profile()
    if profile is None:
        return redirect('profile_create')

    context = {
        'profile': profile,
        'fruits': Fruit.objects.all(),
    }
    return render(request, template_name='core/dashboard.html', context=context)


def fruit_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = FruitCreateForm()

    else:
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, template_name='fruit/create-fruit.html', context=context)


def fruit_details(request, pk):
    profile = get_profile()
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'profile': profile,
        'fruit': fruit,
    }

    return render(request, template_name='fruit/details-fruit.html', context=context)


def fruit_edit(request, pk):
    profile = get_profile()
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitEditForm(instance=fruit)

    else:
        form = FruitEditForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
        'profile': profile,
    }

    return render(request, template_name='fruit/edit-fruit.html', context=context)


def fruit_delete(request, pk):
    profile = get_profile
    fruit = Fruit.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)

    else:
        form = FruitDeleteForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'profile': profile,
        'fruit': fruit
    }

    return render(request, template_name='fruit/delete-fruit.html', context=context)


def profile_create(request):
    profile = get_profile()
    if profile is not None:
        return redirect('index')
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }
    return render(request, template_name='profile/create-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    fruits_count = Fruit.objects.count()

    context = {
        'profile': profile,
        'fruits_count': fruits_count,
    }
    return render(request, template_name='profile/details-profile.html', context=context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)

    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template_name='profile/edit-profile.html', context=context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)

    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, template_name='profile/delete-profile.html', context=context)
