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
            publish = form.save(commit=False)
            publish.role = 1
            publish.save()
            return HttpResponseRedirect('/')
    return render(request, 'user/register.html', {'form':form})

def update_user(request, id):
    user_info = Users.objects.get(id=id)
    if user_info.role == 1:
        form = UpdateUserForm(instance=user_info)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=user_info)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    return render(request, 'user/register.html', {'form':form})

def get_user(request, id):
    user_info = Users.objects.get(id=id)
    return render(request, 'user/user_info.html', {'Data':user_info})

def admin_get_user(request):
    users = Users.objects.all()
    return render(request, 'user/user_list.html', {'Data': users})

def create_admin(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            publish = form.save(commit=False)
            publish.role = 0
            publish.save()
            return HttpResponseRedirect('/')
    return render(request, 'user/register.html', {'form':form})

def update_admin(request, id):
    admin_info = Users.objects.get(id=id)
    if admin_info.role == 0:
        form = UpdateUserForm(instance=admin_info)
        if request.method == 'POST':
            form = UpdateUserForm(request.POST, instance=admin_info)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    return render(request, 'user/register.html', {'form': form})

def admin_delete(request, id):
    user_delete = Users.objects.get(id=id)
    user_delete.delete()
    return HttpResponseRedirect('/')
