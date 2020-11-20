'''Testing Posts Models'''
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

from posts.models import Post
from django.test import RequestFactory
from django.test import Client
from faker import Faker
import pytest
from posts.views import PostList
from . import factories


client = Client()


def test_reqfactory(db):
    factory = RequestFactory()
    request = factory.get('posts/')
    request.user = factories.UserFactory()
    response = PostList.as_view()(request)
    assert 200 == response.status_code


def test_post_detail_page(db):
    '''Тест на наличие страницы comments/<slug:slug>/ и контента в ней'''
    post = factories.PostFactory()
    response = client.get(reverse('posts:detail', args=[post.slug]))
    assert response.status_code == 200
