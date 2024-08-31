from django.utils import timezone
from django.contrib import messages
import random
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientForm, AppointmentForm, MessageForm
from .models import Client, Appointment
from django.http import JsonResponse
from datetime import timedelta

def home(request):
    if request.method == 'POST':
        # login form submission(For now omit code that interact with db)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'home.html', {
                'error': 'Invalid username or password.',
                'greeting': "Welcome",
                'quote': get_random_quote(),
                'current_date': timezone.now(),
                'weather_info': "Sunny with a chance of rain"
            })

        auth_login(request, user)
        return redirect('dashboard')
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

def clients(request):
    clients = Client.objects.all()
    
    context = {
        'clients': clients
    }
    return render(request, 'clients.html', context)

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client created successfully')
            return redirect('clients')
    else:
        form = ClientForm()

    return render(request, 'create_client.html', {'form': form})

def appointments(request):
    appointments = Appointment.objects.all()
    clients = Client.objects.all()
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment created successfully')
            return redirect('appointments')  
    else:
        form = AppointmentForm()
            
    context = {
        'appointments': appointments,
        'clients': clients,
        'form': form
    }
    return render(request, 'appointments.html', context)

def calendar(request):
    appointments = Appointment.objects.all()
    events = [
        {
            'id': appointment.id,
            'title': f"{appointment.client.first_name} {appointment.client.last_name}",
            'start': appointment.date.isoformat(),
            'end': (
                appointment.date + timedelta(hours=1)
            ).isoformat(),  # Assuming 1-hour appointments
            'description': appointment.reason,
        }
        for appointment in appointments
    ]
    
    return render(request, 'calendar.html', {'events': events})
