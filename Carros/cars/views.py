from django.shortcuts import render
from cars.models import Car

def home_view(request):
    cars = Car.objects.all() #selecionar todos os objetos do banco de dados Car
    #print(cars)

    #cars = Car.objects.filter(brand__name='Fiat')

    #cars = Car.objects.filter(model__contains='Chevette')


    return render(
        request,          
        'cars.html', {
        'cars': cars}
    )
