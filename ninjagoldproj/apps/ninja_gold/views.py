from django.shortcuts import render,redirect
from random import randint,choice
import datetime


def index(request):
    if 'counter' not in request.session:
        print('***starting new game***')
        request.session['counter'] = 0

    if 'ninjabank' not in request.session:
        print('***creating bank***')
        request.session['ninjabank'] = 0
        
    if 'action_log' not in request.session:
        print('***creating log***')
        request.session['action_log'] = []

    
    context = {
        "counter": request.session['counter'],
        "log": request.session['action_log'],
        "gold": request.session['ninjabank']
    }
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))
    return render(request, 'ninja_gold/index.html', context)

def process(request, loc):
    print('printing POST')
    print(request.POST)
    action = {
        'Farm': randint(10,20),
        'Cave': randint(5,10),
        'House': randint(2,5),
        'Casino': randint(0,50)*choice([-1,1])
    }
    result = action[request.POST['action']]
    request.session['ninjabank'] += result
    request.session['counter'] += 1
    current_date=datetime.datetime.now()
    current_date = current_date.strftime("%B %d %Y %I:%M:%S %p")
    if result < 0:
        log = "Lost " + str(result) + " gold at the " + request.POST['action']+"! (" +current_date+ ")"
    else:
        log = "Earned " + str(result) + " gold at the " + request.POST['action']+"! (" +current_date+ ")"
    request.session['action_log'].append(log)
    
    return redirect('/')

def reset(request):
    print(request.session)
    print("*"*5 +"RESTTING APP")
    if 'ninjabank' in request.session:
        del request.session['ninjabank']
    if 'action_log' in request.session:    
        del request.session['action_log']
    if 'counter' in request.session:
        del request.session['counter']
    print(request.session)
    return redirect('/')