from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Teacher

import datetime

def index(request):
    date_time = str(datetime.datetime.now())

    template = loader.get_template("test_template.html")
    teachers = Teacher.objects.all().values()

    # for teacher in teachers:
    #     name = teacher["name"]
    #     age = teacher["age"]
    #     output += "<br>"
    #     output += f"name: {name} | age: {age}"

    context = {
        'date_time': date_time,
        'teachers': teachers
    }

    return HttpResponse(template.render(context, request))
