from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm

def cars_view(request):
    cars = Car.objects.all().order_by('model') #selecionar todos os objetos do banco de dados Car
    search = request.GET.get('search')
    #print(cars)

    #cars = Car.objects.filter(brand__name='Fiat')

    if search:
        cars = Car.objects.filter(model__icontains=search)#icontains vai ignorar o uppercase e lowercase

    return render(
        request,          
        'cars.html', {
        'cars': cars}
    )

def new_car_view(request):
    new_car_form = CarForm()
    return render(request, 'new_car.html', { 'new_car_form' : new_car_form})