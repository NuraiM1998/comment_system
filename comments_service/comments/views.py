from django.shortcuts import render
from django.views.generic.edit import CreateView
from comments.forms import CommentForm
from django.urls import reverse_lazy
from posts.models import Post


class CommentCreate(CreateView):
    '''Добавление комментариев'''
    form_class = CommentForm
    template_name = "create_comment.html"
    success_url = reverse_lazy('posts:list')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)