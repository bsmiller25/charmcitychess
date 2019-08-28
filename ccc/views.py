import os
from django.db.models import Sum, Avg, Q, F, Case, Count, When
from django.http import HttpResponse
from django.shortcuts import render
import pdb


def index(request):

    mapbox_key = os.environ.get('MAPBOX_KEY')
    
    context = {
        'mapbox_key': mapbox_key,
    }
    
    return render(
        request,
        'ccc/index.html',
        context
    )

def bylaws(request):

    return render(request, 'ccc/bylaws.html')


def gallery(request, gal_str):

    nice_str = {
        '2019_02_23_Tourney': 'February 2019 Open',
        '2019_06_29_Tourney': 'June 2019 Open'
        }

    tourney = nice_str[gal_str]
    
    photos = ['/static/ccc/gallery/{}/{}'.format(gal_str, i) for i in os.listdir('ccc/static/ccc/gallery/{}/'.format(gal_str))]

    context = {
        'tourney': tourney,
        'photos': photos
        }
    
    return render(
        request,
        'ccc/gallery.html',
        context
    )

def new_tournament(request):
    return render(request, 'ccc/new_tournament.html')
