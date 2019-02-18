from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string


def index(request):
    context = {
        "word": get_random_string(length=14)
    }
    if 'counter' not in request.session:
        print('creating counter')
        request.session['counter'] = 0
        print(request.session['counter'])

    request.session['counter'] += 1
    return render(request, 'random_word/index.html',context)

def reset(request):
    if 'counter' in request.session:
        del request.session['counter']
    return redirect('/random_word')