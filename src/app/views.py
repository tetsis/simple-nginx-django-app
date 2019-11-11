from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def index(request):
    return HttpResponse('This application is "' + settings.APP_NAME + '".')