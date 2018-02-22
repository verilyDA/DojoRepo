from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "Placeholder to later display all blogs"
    return render(request, 'blogs_app/index.html')

def new(request):
    response = 'placeholder to display a new form to create a blog'
    return HttpResponse(response)

def create(request):
    if request.method =="POST":
        print('*'*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name']=request.POST['name']
        print('*'*50)
        return redirect('/')
    else:
        return redirect('/')

def number(request):
    return HttpResponse('blog number page')

def numEdit(request):
    return HttpResponse('blog edit page')

def numDel(request):
    return HttpResponse('blog delete page')
