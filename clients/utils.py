from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from .models import Message, Client, Appointment

def send_email_to_client(message):
    try:
        send_mail(
            subject=f"{message.message_type} Notification",
            message=message.content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[message.client.email],  # Ensure `Client` model has an `email` field
            fail_silently=False,
        )
        message.status = 'Sent'
    except Exception as e:
        message.status = 'Failed'
    message.save()

def create_birthday_message(client):
    content = f"Happy Birthday, {client.first_name} {client.last_name}!"
    Message.objects.create(
        client=client,
        message_type='Birthday',
        content=content,
        status='Pending',
        sent_at=timezone.now()  # Adjust sent_at as needed
    )

def create_christmas_message():
    content = "Merry Christmas from our team!"
    clients = Client.objects.all()
    for client in clients:
        Message.objects.create(
            client=client,
            message_type='Christmas',
            content=content,
            status='Pending',
            sent_at=timezone.now()  # Adjust sent_at as needed
        )

def create_new_year_message():
    content = "Happy New Year from our team!"
    clients = Client.objects.all()
    for client in clients:
        Message.objects.create(
            client=client,
            message_type='New Year',
            content=content,
            status='Pending',
            sent_at=timezone.now()  # Adjust sent_at as needed
        )

def create_appointment_reminder():
    now = timezone.now()
    upcoming_appointments = Appointment.objects.filter(date__date=now.date() + timedelta(days=1))
    for appointment in upcoming_appointments:
        content = f"Reminder: You have an appointment tomorrow at {appointment.date.strftime('%H:%M')}."
        Message.objects.create(
            client=appointment.client,
            message_type='Appointment Reminder',
            content=content,
            status='Pending',
            sent_at=timezone.now()  # Adjust sent_at as needed
        )
