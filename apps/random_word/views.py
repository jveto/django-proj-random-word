from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    response = get_random_string(length=14)
    
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    somevar = 2
    context = {
    "randomWord":get_random_string(length=14),
    "count":request.session['count'],
    "somevar":somevar
    }
    print(request.session['count'])
    return render(request, "random_word/index.html", context)

def reset(request):
    if 'count' in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] = 1
    return redirect('/')
# Create your views here.
