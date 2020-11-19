'''Testing Posts Models'''
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

from faker import Faker
from posts.models import Post
from . import factories
import pytest
