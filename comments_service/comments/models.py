from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """Поля модели Comment"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_post',
        verbose_name='Пользователь'
    )
    content = models.TextField(verbose_name='Контент')
    timestamp = models.DateTimeField(auto_now_add=True, 
                                    verbose_name='Время создания')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                    related_name='comments',
                                    verbose_name='Посты')


    class Meta:
        """Отображаются самые новые комментарии"""
        ordering = ['-timestamp']

    
    def __str__(self):
        return self.content

    
    def get_absolute_url(self):
        """Путь к одному объекту модели Post"""
        return reverse('comments:create_comment', kwargs={'pk': self.pk})
