import os
import datetime
from django.db.models import Sum, Avg, Q, F, Case, Count, When
from django.http import HttpResponse
from django.shortcuts import render
import pdb


def index(request):
    """Charm City Chess Homepage"""
    new_tournament = True
    
    context = {
        'new_tournament': new_tournament,
    }
    
    return render(request, 'ccc/index.html', context)


def bylaws(request):
    """Page for displaying the club bylaws"""
    return render(request, 'ccc/bylaws.html')


def gallery(request, gal_str):
    """Display photo gallery"""
    nice_str = {
        '2019_02_23_Tourney': 'February 2019 Open',
        '2019_06_29_Tourney': 'June 2019 Open',
        '2019_10_12_Tourney': 'October 2019 Open',
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
    """Open registration for a new tournament"""
    done = datetime.datetime.today() > datetime.datetime.strptime('2019-12-14', '%Y-%m-%d')
    earlyreg = datetime.datetime.today() <= datetime.datetime.strptime('2019-12-07', '%Y-%m-%d')
    
    
    context = {
        'done': done,
        'earlyreg': earlyreg
        }
    
    return render(request, 'ccc/new_tournament.html', context)
