from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    context={
    "word": get_random_string(length=25)
    }
    return render(request, "randoWord/index.html", context)
def genny(request):
    context={
    "word": get_random_string(length=25)
    }
    return redirect('/')
