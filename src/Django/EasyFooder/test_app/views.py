from django.http import HttpResponse
from django.template import loader

# import logging
# logger = logging.getLogger("django")
# logger.info("test info")

from .models import Teacher

import datetime
import random


def index(request):
    date_time = str(datetime.datetime.now())

    template = loader.get_template("test_template.html")

    # Adding/Removing teacher
    if request.method == "POST":
        # Adding teacher
        try:
            if "Add" in request.POST:
                name = request.POST.get("name")

                new_teacher = Teacher(name=name, age=random.randint(20, 999))
                new_teacher.save()
            # Removing teacher
            elif "Remove" in request.POST:
                id = request.POST.get("id")
                removed_teacher = Teacher.objects.get(id=id)
                removed_teacher.delete()
        except:
            pass

    teachers = Teacher.objects.all().values()

    context = {
        "date_time": date_time,
        "teachers": teachers
    }

    return HttpResponse(template.render(context, request))


# def add(request):
#     template = loader.get_template("add.html")
#     name = request.POST["new_name"]

#     return HttpResponse(template.render(context, request))
#     # logger.info("test info")

#     return HttpResponse(template.render({}, request))
