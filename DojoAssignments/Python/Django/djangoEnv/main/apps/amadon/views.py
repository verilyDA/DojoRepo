from django.shortcuts import render, HttpResponse, redirect
def index(request):
    response = "Hello, I am your first request!"
    if 'money' not in request.session:
        request.session['money'] = 0
    return render(request, "amadon/index.html")

def process(request):
    request.session['money'] +=50
    response = "Hello, I am your first request!"
    return redirect("/amadon/checkout")

def checkout(request):
    response = "Hello, I am your first request!"
    return render(request, "amadon/checkout.html")
