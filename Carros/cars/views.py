from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View

class CarsView(View):
    
    def get(self, request):
        cars = Car.objects.all().order_by('model') #selecionar todos os objetos do banco de dados Car
        search = request.GET.get('search')
        #cars = Car.objects.filter(brand__name='Fiat')

        if search:
            cars = Car.objects.filter(model__icontains=search)#icontains vai ignorar o uppercase e lowercase

        return render(
            request,          
            'cars.html', {
            'cars': cars}
        )

class NewCarView(View):

    def post(self, request):
        ...
         
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', { 'new_car_form' : new_car_form})

