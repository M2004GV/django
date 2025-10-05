from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
  
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    paginate_by = 3                     # Define o número de itens por página

    def get_queryset(self):
        queryset = super().get_queryset().select_related('brand').order_by('model') # Otimiza a consulta para buscar a marca relacionada
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search) # Filtra os carros pelo modelo, ignorando maiúsculas/minúsculas

        return queryset

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'

class CarDetailView(DetailView):
    model = Car 
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'