from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "rca/01-comming-soon.html")
