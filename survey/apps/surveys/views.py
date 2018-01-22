from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if request.method == 'POST':
        try:
            request.session['counter'] += 1
        except KeyError:
            request.session['counter'] = 1

        request.session['name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']

        return result(request)

def result(request):
    return render(request, 'surveys/result.html')
