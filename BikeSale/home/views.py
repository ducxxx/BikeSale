from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import BikeForm
from .models import Bike

# Create your views here.
def create_bike(request):
    form = BikeForm()
    if request.method == 'POST':
        form = BikeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'bike/create_bike.html', {'form':form})

def update_bike(request, id):
    bike = Bike.objects.get(id=id)
    if request.method == 'POST':
        form = BikeForm(request.POST, instance=bike)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'bike/create_bike.html', {'form': form})

def get_bike(request):
    bikes = Bike.objects.all()
    return render(request, 'bike/home.html', {'bikes': bikes})

def delete_bike(request, id):
    bike = Bike.objects.get(id=id)
    bike.delete()
    return HttpResponseRedirect('/')