from django.shortcuts import render

def home_view(request):
    return render(
        request,          
        'cars.html', {
        'cars':{'model':'Astra 2.0'}}
    )
