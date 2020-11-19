import datetime
import factory
from posts.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = Post

    title = factory.Sequence(lambda n: 'Title{0}'.format(n))
    slug = factory.Sequence(lambda n: 'Slug{0}'.format(n))
    body = factory.Sequence(lambda n: 'Body{0}'.format(n))
    date_pub = factory.LazyFunction(datetime.datetime.now)
