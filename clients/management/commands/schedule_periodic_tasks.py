from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import timedelta

class Command(BaseCommand):
    help = 'Schedule periodic tasks'

    def handle(self, *args, **kwargs):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,  # Run every 10 minutes
            period=IntervalSchedule.MINUTES
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Send scheduled messages',
            task='clients.tasks.send_scheduled_messages'
        )

        self.stdout.write(self.style.SUCCESS('Scheduled periodic task'))
