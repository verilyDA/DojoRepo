from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
    return render(request, "dojoGold/index.html")

def gold(request, source):
    print(source)
    act_list = request.session['activity']

    if source == 'farm':
        gold = random.randint(10, 20)
        request.session['gold'] += gold
        string1 = 'Earned {} gold from the {} ({})'.format(gold, source, strftime("%Y-%m-%d %H:%M %p", gmtime()))

    if source == 'cave':
        gold = random.randint(5,10)
        request.session['gold'] += gold
        string1 = 'Earned {} gold from the {} ({})'.format(gold, source, strftime("%Y-%m-%d %H:%M %p", gmtime()))

    if source == 'house':
        gold = random.randint(2,5)
        request.session['gold'] += gold
        string1 = 'Earned {} gold from the {} ({})'.format(gold, source, strftime("%Y-%m-%d %H:%M %p", gmtime()))

    if source == 'casino':
        if random.randint(0,1) == 1:
            gold = random.randint(0,50)
            request.session['gold'] += gold
            string1 = 'Earned {} gold from the {} ({})'.format(gold, source, strftime("%Y-%m-%d %H:%M %p", gmtime()))
        else:
            gold = random.randint(0,50)
            request.session['gold'] -= gold
            string1 = 'Lost {} gold from the {} ({})'.format(gold, source, strftime("%Y-%m-%d %H:%M %p", gmtime()))


    act_list.append(string1)
    request.session['activity']=act_list


    return redirect('/')

def clear(request):
    request.session.flush()
    return redirect('/')
