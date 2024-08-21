from datetime import timezone
import random
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'POST':
        # login form submission(For now omit code that interact with db)
        username = request.POST.get('username')
        password = request.POST.get('password')
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
            #auth_login(request, user)
        return redirect('dashboard')
        #else:
            #return render(request, 'home.html', {
                #'error': 'Invalid username or password.',
                #'greeting': "Welcome",
                #'quote': get_random_quote(),
                #'current_date': timezone.now(),
                #'weather_info': "Sunny with a chance of rain"
            #})

    #Home Page Context
    context = {
        'greeting': "Welcome",
        'quote': get_random_quote(),
        'current_date': "",
        'weather_info': "Sunny with a chance of rain"
    }
    return render(request, 'home.html', context)

def get_random_quote():
    quotes = [
        "Health is wealth.",
        "An apple a day keeps the doctor away.",
        "Take care of your body. It's the only place you have to live.",
        "Your health is your greatest asset.",
        "A healthy outside starts from the inside."
    ]
    return random.choice(quotes)

#@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
