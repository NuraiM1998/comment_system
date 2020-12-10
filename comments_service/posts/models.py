from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()

class Post(models.Model):
    """Поля модели Post"""
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="post_set",
        null=True
    )
    title = models.CharField(max_length=150,
                            verbose_name='Название поста')
    slug = models.SlugField(max_length=150,
                            verbose_name='Слаг поста',
                            blank=True)
    body = models.TextField(blank=True,
                            verbose_name='Описание поста')
    date_pub = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Время создания поста')
    favorite = models.ManyToManyField(
        User, 
        related_name="favorite_set",
        blank=True,
        null=True
    )


    def get_absolute_url(self):
        """Путь к одному объекту модели Post"""
        return reverse('posts:detail', kwargs={'slug': self.slug})


    def __str__(self):
        """Отображение название объекта"""
        return self.title

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

