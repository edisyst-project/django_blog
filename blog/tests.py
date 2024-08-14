from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            author="Test Author"
        )

    def test_post_content(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "Test Content")
        self.assertEqual(self.post.author, "Test Author")

class PostDetailViewTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content",
            author="Test Author"
        )

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get(f'/post/{self.post.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
