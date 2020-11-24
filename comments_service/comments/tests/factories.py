
from django.contrib.auth.models import User
import datetime
from comments.models import Comment
from posts.tests.factories import PostFactory
import factory


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('name')
    first_name = factory.Sequence(
                    lambda n: 'Nurai{0}'.format(n)
                )
    last_name = factory.Sequence(
                    lambda n: 'Maratova{0}'.format(n)
                )
    email = factory.Sequence(
                    lambda n: 'email{0}@gmail.com'.format(n)
                )


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    content = factory.Faker('name')
    timestamp = factory.LazyFunction(datetime.datetime.now)
    post = factory.SubFactory(PostFactory)
