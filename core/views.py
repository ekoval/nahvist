from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    ctx = RequestContext(request, {})
    return render_to_response('base.html', ctx)

