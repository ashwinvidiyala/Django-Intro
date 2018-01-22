from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
    "time": strftime("%Y-%m-%d %H-%M %P", gmtime())
    }
    return render(request, 'first_app/index.html', context)
