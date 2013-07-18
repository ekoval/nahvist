from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from core.forms import TripForm
from django.contrib.auth.decorators import login_required
from core.models import Trip


def about_project(request):
    ctx = RequestContext(request, {})
    return render_to_response('about.html', ctx)


@login_required
def new_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, user=request.user)
        if form.is_valid():
            form.instance.host = request.user
            form.save()

    else:
        form = TripForm(user=request.user)

    ctx = RequestContext(request, {'form': form})
    return render_to_response('trip.html', ctx)

def find_trip(request):
    ctx = RequestContext(request, {})
    return render_to_response('about.html', ctx)


def my_trips(request):
    ctx = RequestContext(request, {})
    return render_to_response('about.html', ctx)


def my_requests(request):
    ctx = RequestContext(request, {})
    return render_to_response('about.html', ctx)


def find_trips(request):
    ctx = RequestContext(request, {})
    return render_to_response('about.html', ctx)


def logout_user(request):
    logout(request)
