from django.shortcuts import render
from django.http import HttpResponse


def index(request):
#    context = "<h1> Home Page</h1>"
    return render (request, 'pages/index.html')


def about(request):
#    context = "<h1> About Page </h1>"
    return render (request, 'pages/about.html')
