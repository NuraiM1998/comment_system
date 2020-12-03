from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from posts.models import Post
from posts.tests.factories import PostFactory
import pytest


client = APIClient()

def test_post_list(db):
    url = reverse("post_api:post-list")
    post = PostFactory()
    response = client.get(url)

    assert len(response.json()) == 1
    assert response.status_code == 200


def test_post_detail_page(db):
    '''
    Тест на наличие страницы comments/<slug:slug>/ 
    и контента в ней
    '''
    post = PostFactory()
    response = client.get(reverse('post_api:post-detail', args=[post.slug]))
    assert response.status_code == 200
