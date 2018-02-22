from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    if 'list' not in request.session:
        request.session['list'] = []
    return render(request, "sessionWords/index.html")

def process(request):

    form_list = request.session['list']
    form_list.append([request.POST['word'], request.POST['color'], request.POST['big'], strftime("%Y-%m-%d %H:%M %p", gmtime())])
    request.session['form']=form_list

    return redirect('/sessionWords')

def clear(request):
    request.session.flush()
    return redirect('/sessionWords')
