from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse("<h1> Hello, world this is a first edit.")
    return render(request,"index.html")