from django.core.management.base import BaseCommand
from blog.models import create_fake_posts  # Import corretto

class Command(BaseCommand):
    help = 'Popola il database con post e tag fake per testare l\'applicazione'

    def handle(self, *args, **kwargs):
        create_fake_posts(10)  # Puoi modificare il numero secondo necessità
        self.stdout.write(self.style.SUCCESS('Database popolato con post e tag di test!'))
