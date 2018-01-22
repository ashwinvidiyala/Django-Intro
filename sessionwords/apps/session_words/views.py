from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime

def session_words(request):
    return render(request, 'session_words/index.html')

def add(request):
    form_info = []
    if request.method == 'POST':
        request.session['word'] = request.POST['word']
        request.session['color'] = request.POST['color']
        if 'big_font' in request.POST:
            request.session['big_font'] = request.POST['big_font']

        request.session['time'] = strftime("%H-%M %P, %m-%d-%Y", gmtime())

        return render(request, 'session_words/index.html')

def delete(request):
    if request.method == 'POST':
        try:
            del request.session['word']
            del request.session['color']
            del request.session['big_font']
            del request.session['time']
        except KeyError:
            pass
        return render(request, 'session_words/index.html')
            # return session_words(request)
