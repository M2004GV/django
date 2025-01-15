from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

def register_view(request):
    user_forms = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_forms})
