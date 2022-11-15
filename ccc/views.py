import os
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg, Q, F, Case, Count, When
from django.http import HttpResponse
from django.shortcuts import render, redirect
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import *
from .forms import *
import pdb

new_tournament = True
special_event = True

# tournament
tname = 'Charm City Chess Club 2022 December Open Tournament'
tdate = datetime.datetime.strptime('2022-12-04', '%Y-%m-%d').date()
edate = datetime.datetime.strptime('2022-11-27', '%Y-%m-%d').date()


if tdate < datetime.date.today():
    new_tournament = False

#special event
sename = '"The Exterminator" Simultaneous Exhibition'
sedate = datetime.datetime.strptime('2022-12-18', '%Y-%m-%d').date()

if sedate < datetime.date.today():
    special_event = False

def send_email(to_emails, bcc_emails, subj, msg):
    message = Mail(
        from_email=('charmcitychess@charmcitychess.com', 'Charm City Chess'),
        to_emails=to_emails,
        subject=subj,
        html_content=msg)

    message.reply_to = 'bsmiller25@gmail.com'
    message.bcc = bcc_emails

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API'))
        response = sg.send(message)
    except Exception as e:
        print(e.message)


def index(request, new_tournament=new_tournament, special_event=special_event, tdate=tdate):
    """Charm City Chess Homepage"""
    new_tournament = new_tournament
    special_event = special_event
    tdate = tdate
    sedate = sedate

    context = {
        'new_tournament': new_tournament,
        'special_event': special_event,
        'tdate': tdate,
        'sedate': sedate,
    }

    return render(request, 'ccc/index.html', context)


@login_required
def profile(request):
    """User's profile page"""
    if request.method == 'POST':
        member = Member.objects.get(user=request.user)
        if request.POST.get('uscf_id'):
            member.uscf_id = request.POST.get('uscf_id')
        if request.POST.get('chesscom_id'):
            member.chesscom_id = request.POST.get('chesscom_id')
        if request.POST.get('lichess_id'):
            member.lichess_id = request.POST.get('lichess_id')
        member.save()

    return render(request, 'ccc/profile.html')


def register(request):
    """user registration"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def members(request):
    """list all members"""
    members = Member.objects.all()

    context = {
        'members': members
    }
    return render(request, 'ccc/members.html', context)


def coaching(request):
    """Help find coaching"""
    coaches = Coach.objects.all()

    context = {
        'coaches': coaches,
    }
    return render(request, 'ccc/coaches.html', context)


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

    photos = ['/static/ccc/gallery/{}/{}'.format(gal_str, i) for i in os.listdir(
        'ccc/static/ccc/gallery/{}/'.format(gal_str))]

    context = {
        'tourney': tourney,
        'photos': photos
    }

    return render(
        request,
        'ccc/gallery.html',
        context
    )


def new_tournament(request, tname=tname, tdate=tdate, edate=edate):
    """Open registration for a new tournament"""

    tname = tname
    tdate = tdate
    edate = edate

    done = datetime.datetime.today().date() + datetime.timedelta(days=1) > tdate
    earlyreg = datetime.datetime.today().date() <= edate

    context = {
        'tname': tname,
        'done': done,
        'earlyreg': earlyreg,
        'tdate': tdate,
        'edate': edate,
    }

    return render(request, 'ccc/new_tournament.html', context)

def special_event(request, sename=sename, sedate=sedate):
    
    sedone = datetime.datetime.today().date() + datetime.timedelta(days=1) > sedate
    
    context = {
        'sename': sename,
        'sedate': sedate,
        'sedone': sedone,
        }

    return render(request, 'ccc/special_event.html', context)
