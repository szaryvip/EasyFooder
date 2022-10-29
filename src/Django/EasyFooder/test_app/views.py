from django.shortcuts import render
from django.http import HttpResponse

import datetime

def index(request):
    return HttpResponse(datetime.datetime.now())
