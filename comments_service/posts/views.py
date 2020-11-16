from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from posts.models import Post
from comments.models import Comment
from comments.forms import CommentForm


class PostList(ListView):
    """Список объектов модели Post"""
    model = Post
    template_name = 'post_list.html'


    def get_queryset(self):
        return Post.objects.order_by('date_pub').reverse()


class PostDetail(DetailView):
    """
    один объект Post,
    и список комментариев с вложенностью
    и пагинацией
    """
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('posts:list')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug', None)
        post = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=post)
        comment_form = CommentForm(user=self.request.user,
                                    initial={
                                        'user': self.request.user, 
                                        })
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form
        }
        return context


    def form_valid(self, form):
        model_instance = form.save(commit=False)
        model_instance.post = self.object
        model_instance.save()
        return redirect(self.success_url)
