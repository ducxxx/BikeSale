from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import BikeDetailForm
from django.http import HttpResponseRedirect
from .models import BikeDetail

# Create your views here.
def create_bike_detail(request):
    form = BikeDetailForm()
    if request.method == 'POST':
        form = BikeDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'bike_detail/create_bike.html', {'form':form})

def update_bike_detail(request, id):
    bike_detail = BikeDetail.objects.get(id=id)
    if request.method == 'POST':
        form = BikeDetailForm(request.POST, instance=bike_detail)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'bike_detail/create_bike.html', {'form':form})

def delete_bike_detail(request, id):
    bike_detail = BikeDetail.objects.get(id=id)
    bike_detail.delete()
    return HttpResponseRedirect('/')

def get_bike_detail(request, id):
    bike = BikeDetail.objects.get(id=id)
    return render(request, 'bike_detail/bike_detail.html', {'bike':bike})