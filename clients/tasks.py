from celery import shared_task
from django.utils import timezone
from .models import Message
from .utils import send_email_to_client

@shared_task
def send_scheduled_messages():
    now = timezone.now()
    messages = Message.objects.filter(status='Pending', sent_at__lte=now)
    for message in messages:
        send_email_to_client(message)
        message.status = 'Sent'
        message.save()
