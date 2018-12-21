import os
from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    mapbox_key = os.environ.get('MAPBOX_KEY')
    
    context = {
        'mapbox_key': mapbox_key
        }
    
    return render(request, 'ccc/index.html', context)
