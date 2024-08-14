from django.core.management.base import BaseCommand
from blog.models import create_fake_posts

class Command(BaseCommand):
    help = 'Crea post fake per testare l\'applicazione'

    def handle(self, *args, **kwargs):
        create_fake_posts(10)
        self.stdout.write(self.style.SUCCESS('10 post fake sono stati creati con successo.'))
