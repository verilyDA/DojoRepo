from django.shortcuts import render, HttpResponse, redirect
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, "surveyForm/index.html")
def form(request):
    if request.method == "POST":
        request.session['count'] += 1
        context = {
            'name':request.POST['name'],
            'loc':request.POST['loc'],
            'lang':request.POST['lang'],
            'com':request.POST['com']
        }
        return render(request, "surveyForm/result.html", context)
    else:
        return redirect("/surveyForm")
