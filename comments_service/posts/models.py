from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse


class Post(models.Model):
    """Поля модели Post"""
    title = models.CharField(max_length=150,
                            verbose_name='Название поста')
    slug = models.SlugField(max_length=150,
                            verbose_name='Слаг поста',
                            blank=True)
    body = models.TextField(blank=True,
                            verbose_name='Описание поста')
    date_pub = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Время создания поста')


    def get_absolute_url(self):
        """Путь к одному объекту модели Post"""
        return reverse('posts:detail', kwargs={'slug': self.slug})


    def __str__(self):
        """Отображение название объекта"""
        return str(self.title)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
