from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return render(request, 'amadon/index.html')

def buy(request):
    if request.method == 'POST':
        print request.POST['product_id']
        if request.POST['product_id'] == '1015':
            request.session['price'] = 19.99
            request.session['name'] = 'Dojo Tshirt'
            print request.session['price']
        if request.POST['product_id'] == '1016':
            request.session['price'] = 29.99
            request.session['name'] = 'Dojo Sweater'
        if request.POST['product_id'] == '1017':
            request.session['price'] = 4.99
            request.session['name'] = 'Dojo Cup'
        if request.POST['product_id'] == '1018':
            request.session['price'] = 49.99
            request.session['name'] = 'Algorithm Book'

        # print request.session['price']
        request.session['quantity'] = int(request.POST['quantity'])

        return redirect('/amadon/checkout')
        # return HttpResponse('hi')
        # return render(request, 'amadon/checkout.html')

def checkout(request):
    if 'total_price' and 'total_quantity' not in request.session:
        request.session['total_price'] = 0
        request.session['total_quantity'] = 0
    else:
        request.session['total_price'] += request.session['price']
        request.session['total_quantity'] += request.session['quantity']

    return render(request, 'amadon/checkout.html')
