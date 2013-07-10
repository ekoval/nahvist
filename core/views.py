from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import logout


def about_project(request):
    ctx = RequestContext(request, {})
    return render_to_response('about.html', ctx)


def new_trip(request):
    ctx = RequestContext(request, {})
    return render_to_response('about.html', ctx)


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
