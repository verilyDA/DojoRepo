from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
    'email':'test@email.com',
    'name':'test name'
    }
    return render(request, 'first_app/index.html', context)
