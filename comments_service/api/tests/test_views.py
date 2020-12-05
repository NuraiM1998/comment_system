from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from posts.models import Post
from posts.tests.factories import PostFactory
from comments.tests.factories import CommentFactory
import pytest


client = APIClient()

def test_post_list(db):
    url = reverse("post_api:post-list")
    post = PostFactory()
    response = client.get(url)

    assert len(response.json()) == 1
    assert response.status_code == 200


def test_post_detail_page(db):
    post = PostFactory()
    response = client.get(reverse('post_api:post-detail', args=[post.slug]))
    assert response.status_code == 200


def test_comment_list(db):
    url = reverse("post_api:post-comment-list", kwargs={"slug": "slug"})
    post = PostFactory()
    comment = CommentFactory()
    response = client.get(url)

    assert response.status_code == 200

