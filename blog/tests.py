from django.test import TestCase
from .models import Category, Post
from django.contrib.auth.models import User


class HomeViewTest(TestCase):

    def test_home_returns_200(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)


class PublishedPostsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        self.category = Category.objects.create(
            name='Django',
            slug='django'
        )

    def test_published_post_appears_on_home(self):
        Post.objects.create(
            title='Post publicado',
            slug='post-publicado',
            content='Conteúdo do post.',
            author=self.user,
            category=self.category,
            published_at='2026-01-01T10:00:00Z'
        )

        response = self.client.get('/')

        self.assertContains(
            response,
            'Post publicado'
        )

    def test_draft_post_does_not_appear_on_home(self):
        Post.objects.create(
            title='Post rascunho',
            slug='post-rascunho',
            content='Conteúdo do rascunho.',
            author=self.user,
            category=self.category,
            published_at=None
        )

        response = self.client.get('/')

        self.assertNotContains(
            response,
            'Post rascunho'
        )


class PostCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )

        self.category = Category.objects.create(
            name='Django',
            slug='django'
        )

    def test_anonymous_user_cannot_create_post(self):
        response = self.client.get('/post/create/')

        self.assertEqual(
            response.status_code,
            302
        )

    def test_authenticated_user_can_create_post(self):
        self.client.login(
            username='testuser',
            password='testpassword123'
        )

        response = self.client.post(
            '/post/create/',
            {
                'title': 'Meu primeiro Post',
                'slug': 'meu-primeiro-post',
                'content': 'Conteúdo do Post.',
                'category': self.category.id,
                'tags': [],
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.assertTrue(
            Post.objects.filter(
                title='Meu primeiro Post'
            ).exists()
        )


class PostOwnershipTest(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(
            username='author',
            password='authorpassword123'
        )

        self.other_user = User.objects.create_user(
            username='other',
            password='otherpassword123'
        )

        self.category = Category.objects.create(
            name='Python',
            slug='python'
        )

        self.post = Post.objects.create(
            title='Post do autor',
            slug='post-do-autor',
            content='Conteúdo original.',
            author=self.author,
            category=self.category
        )

    def test_author_can_edit_own_post(self):
        self.client.login(
            username='author',
            password='authorpassword123'
        )

        response = self.client.post(
            '/post/post-do-autor/edit/',
            {
                'title': 'Post atualizado',
                'slug': 'post-do-autor',
                'content': 'Conteúdo atualizado.',
                'category': self.category.id,
                'tags': [],
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )

        self.post.refresh_from_db()

        self.assertEqual(
            self.post.title,
            'Post atualizado'
        )

    def test_other_user_cannot_edit_post(self):
        self.client.login(
            username='other',
            password='otherpassword123'
        )

        response = self.client.post(
            '/post/post-do-autor/edit/',
            {
                'title': 'Tentativa de alteração',
                'slug': 'post-do-autor',
                'content': 'Não deveria funcionar.',
                'category': self.category.id,
                'tags': [],
            }
        )

        self.assertEqual(
            response.status_code,
            403
        )

        self.post.refresh_from_db()

        self.assertEqual(
            self.post.title,
            'Post do autor'
        )

    def test_other_user_cannot_delete_post(self):
        self.client.login(
            username='other',
            password='otherpassword123'
        )

        response = self.client.post(
            '/post/post-do-autor/delete/'
        )

        self.assertEqual(
            response.status_code,
            403
        )

        self.assertTrue(
            Post.objects.filter(
                pk=self.post.pk
            ).exists()
        )