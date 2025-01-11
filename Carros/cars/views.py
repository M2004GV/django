from django.shortcuts import render
from cars.models import Car

def home_view(request):
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
