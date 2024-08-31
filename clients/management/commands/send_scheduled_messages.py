from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from clients.utils import create_birthday_message, create_christmas_message, create_new_year_message, create_appointment_reminder
from clients.models import Client
class Command(BaseCommand):
    help = 'Schedule messages for birthdays, holidays, and appointments'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        
        # Schedule birthday messages
        clients_birthday_today = Client.objects.filter(birthday__month=now.month, birthday__day=now.day)
        for client in clients_birthday_today:
            create_birthday_message(client)

        # Schedule Christmas and New Year messages
        create_christmas_message()
        create_new_year_message()

        # Schedule appointment reminders
        create_appointment_reminder()

        self.stdout.write(self.style.SUCCESS('Scheduled messages for today'))
