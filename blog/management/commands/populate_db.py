from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Popola il database con post fake.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indica il numero di post da creare')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        # Recupera un utente esistente o crea un nuovo utente fittizio
        user = User.objects.first()  # Modifica per selezionare un autore specifico o crearne uno

        if not user:
            user = User.objects.create_user('fakeuser', 'fake@example.com', 'password123')

        for _ in range(total):
            title = fake.sentence(nb_words=6)
            content = fake.paragraph(nb_sentences=5)
            Post.objects.create(
                title=title,
                content=content,
                author=user
            )

        self.stdout.write(self.style.SUCCESS(f'Creati {total} post fake.'))
