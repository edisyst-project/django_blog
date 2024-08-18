from django.test import TestCase
from django.urls import reverse
from blog.models import Post, Tag
from django.contrib.auth.models import User

class PostListViewTest(TestCase):
    def setUp(self):
        # Creazione di un utente fittizio
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Creazione dei tag fittizi
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')

        # Creazione di post fittizi
        self.post1 = Post.objects.create(title='Test Post 1', content='Test content 1', author=self.user)
        self.post1.tags.add(self.tag1)

        self.post2 = Post.objects.create(title='Test Post 2', content='Test content 2', author=self.user)
        self.post2.tags.add(self.tag2)

    def test_tag_filter_functionality(self):
        # Testa il filtro per tag
        response = self.client.get(reverse('post-list'), {'tag': self.tag1.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

class PostModelTest(TestCase):
    def setUp(self):
        # Creazione di un utente fittizio
        self.user = User.objects.create_user(username='author1', password='testpass')

        # Creazione di post fittizi
        self.post1 = Post.objects.create(title='Test Post 1', content='Test content 1', author=self.user)
        self.post2 = Post.objects.create(title='Test Post 2', content='Test content 2', author=self.user)

    def test_post_creation(self):
        # Verifica che i post siano stati creati correttamente
        self.assertEqual(self.post1.title, 'Test Post 1')
        self.assertEqual(self.post2.title, 'Test Post 2')
