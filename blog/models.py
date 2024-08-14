from django.db import models
from django.utils import timezone
from faker import Faker

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    fake = Faker()
    def create_fake_posts(n=5):
        for _ in range(n):
            Post.objects.create(
                title=fake.sentence(),
                content=fake.paragraph(),
                author=fake.name()
            )
