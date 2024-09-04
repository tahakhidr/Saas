from django.shortcuts import render

from .models import *


def home(request):
    PageVisit.objects.create(path=request.path)

    return render(request, "core/home.html")
