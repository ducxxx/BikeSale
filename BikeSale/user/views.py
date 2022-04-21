from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .form import CreateUserForm, UpdateUserForm
from .models import Users

# Create your views here.
def create_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.role = 1
            publish = form.save()
            publish.save()
            return HttpResponseRedirect('/')
    return render(request, 'link page register', {'form':form})

def update_user(request, id):
    user_info = Users.objects.get(id=id)
    form = UpdateUserForm(instance=user_info)
    if request.method == 'PUT':
        form = UpdateUserForm(request.PUT, instance=user_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'link page update info', {'form': form})

def admin_get_user(request):
    users = Users.objects.all()
    return render(request, 'admin get list user', {'Data': users})

def create_admin(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.role = 0
            publish = form.save()
            publish.save()
            return HttpResponseRedirect('/')
    return render(request, 'link page register', {'form':form})

def update_admin(request, id):
    admin_info = Users.objects.get(id=id)
    form = UpdateUserForm(instance=admin_info)
    if request.method == 'PUT':
        form = UpdateUserForm(request.PUT, instance=admin_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'link page update info', {'form': form})

def admin_delete(request, id):
    user_delete = Users.objects.get(id=id)
    user_delete.delete()
    return HttpResponseRedirect('/')
