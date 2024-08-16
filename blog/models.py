from django.db import models
from django.utils import timezone
from faker import Faker
import random
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Modello per rappresentare i tag associati ai post.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Modello per rappresentare un post del blog.
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Modello per rappresentare un commento su un post del blog.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"




# Funzione per creare tag fake
def create_fake_tags(n=5):
    fake = Faker()
    tags = []
    for _ in range(n):
        tag = Tag.objects.create(name=fake.word())
        tags.append(tag)
    return tags

# Funzione per creare post fake e assegnare tag
def create_fake_posts(n=5):
    fake = Faker()
    tags = create_fake_tags()  # Crea e recupera i tag fake
    for _ in range(n):
        post = Post.objects.create(
            title=fake.sentence(),
            content=fake.paragraph(),
        )
        # Associa da 0 a 2 tag randomicamente
        random_tags = random.sample(tags, k=random.randint(0, 2))
        post.tags.set(random_tags)