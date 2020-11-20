import datetime
import factory
from posts.models import Post
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker('name')
    first_name = factory.Sequence(lambda n: 'Nurai{0}'.format(n))
    last_name = factory.Sequence(lambda n: 'Maratova{0}'.format(n))
    email = factory.Sequence(lambda n: 'email{0}@gmail.com'.format(n))



class PostFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: 'Title{0}'.format(n))
    slug = factory.Sequence(lambda n: 'Slug{0}'.format(n))
    body = factory.Sequence(lambda n: 'Body{0}'.format(n))
    date_pub = factory.LazyFunction(datetime.datetime.now)
