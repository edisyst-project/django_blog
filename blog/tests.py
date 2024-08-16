from django.test import TestCase
from django.urls import reverse
from .models import Post, Tag

class PostModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name='tag1')
        self.post1 = Post.objects.create(title='Test Post 1', content='Test content 1', author='Author 1')
        self.post1.tags.add(self.tag1)

    def test_post_creation(self):
        self.assertEqual(self.post1.title, 'Test Post 1')
        self.assertEqual(self.post1.content, 'Test content 1')
        self.assertEqual(self.post1.tags.first().name, 'tag1')

class PostListViewTest(TestCase):
    def setUp(self):
        tag1 = Tag.objects.create(name='tag1')
        tag2 = Tag.objects.create(name='tag2')
        self.post1 = Post.objects.create(title='Test Post 1', content='Test content 1')
        self.post1.tags.set([tag1])
        self.post2 = Post.objects.create(title='Test Post 2', content='Test content 2')
        self.post2.tags.set([tag2])

    def test_post_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post 1')
        self.assertContains(response, 'Test Post 2')

    def test_search_functionality(self):
        response = self.client.get(reverse('post-list'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post 1')

    def test_tag_filter_functionality(self):
        response = self.client.get(reverse('post-list'), {'tag': [self.tag1.id]})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post 1')
