from django.shortcuts import render
from django.http import HttpResponse
from .models import Teachers

import datetime

def index(request):
    output = str(datetime.datetime.now())
    teachers = Teachers.objects.all().values()
    for teacher in teachers:
        name = teacher["name"]
        age = teacher["age"]
        output += "<br>"
        output += f"name: {name} | age: {age}"
    return HttpResponse(output)
