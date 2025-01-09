from django.shortcuts import render
from cars.models import Car

def home_view(request):
    cars = Car.objects.all()#selecionar todos os objetos do banco de dados Car
    #print(cars)

    return render(
        request,          
        'cars.html', {
        'cars': cars}
    )
