from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth import logout
from core.forms import TripForm
from django.contrib.auth.decorators import login_required
from core.models import DriverTrip
from core import constants


def about_project(request):
    return render(request, 'about.html')


@login_required
def new_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, user=request.user)
        if form.is_valid():
            form.instance.host = request.user
            if not form.instance.id:
                form.instance.state = constants.TRIP_STATE_PLANNED
            form.save()

    else:
        form = TripForm(user=request.user)

    return render(request, 'trip.html', {'form': form})

def find_trip(request):
    trips = DriverTrip.objects.exclude(user=request.user)
    return render(request, 'find_trip.html', {'trips': trips})


def my_trips(request):
    organized_by_myself = DriverTrip.objects.filter(user=request.user)
    return render(request, 'my_trips.html', {'organized_by_myself': organized_by_myself})


def my_requests(request):
    return render(request, 'about.html')


def find_trips(request):
    return render(request, 'about.html')


def logout_user(request):
    logout(request)
