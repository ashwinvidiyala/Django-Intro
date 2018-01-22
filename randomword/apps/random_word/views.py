from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'random_word/index.html')

def create(request):
    if request.method == 'POST':
        try:
            request.session['counter']
        except KeyError:
            request.session['counter'] = 0
        request.session['counter'] += 1
        context = {
            'random_word': get_random_string(length = 14),
        }
        return render(request, "random_word/index.html", context)
    else:
        return redirect('/')

def reset(request):
    try:
        del request.session['counter']
    except KeyError:
        pass
        
    return create(request)
