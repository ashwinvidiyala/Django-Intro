from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return HttpResponse('placeholder for users to create a new user record')

def users(request):
    return HttpResponse('placeholder to later display all the list of users')

def login(request):
    return HttpResponse('placeholder for users to login')
