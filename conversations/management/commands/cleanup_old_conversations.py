from django.core.management.base import BaseCommand
from django.utils import timezone
from conversations.models import Conversation
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Clean up conversations older than a specified number of days'

    def add_arguments(self, parser):
        parser.add_argument('days', type=int, help='The number of days to keep conversations')

    def handle(self, *args, **kwargs):
        days = kwargs['days']
        cutoff_date = datetime.now() - timedelta(days=days)
        old_conversations = Conversation.objects.filter(date__lt=cutoff_date)
        old_conversations.delete()
        self.stdout.write(f'Deleted conversations older than {days} days')

