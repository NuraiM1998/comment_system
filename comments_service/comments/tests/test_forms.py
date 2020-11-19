'''Testing Comments'''
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from comments.models import Comment
from comments.forms import CommentForm

from faker import Faker
from . import factories
import pytest



@pytest.mark.parametrize(
    'user, post_id, content, validity',
    [
     ('username1', 1, 'Some content',  True),
     ('me5@mail.ru', 2,  '',  False),
     (None, 0,  None, False),
    ])
def test_example_form(db, user, content, post_id, validity):
    comment = factories.CommentFactory()
    comment_user = comment.user
    comment_post_id = comment.post_id
    form = CommentForm(user=comment_user, post_id=comment_post_id, data={
        'user': user,         
        'content': content,
        'post_id': comment_post_id
    })

    assert form.is_valid() is validity
