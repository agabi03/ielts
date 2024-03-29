from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import ArticleForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'materials/article_list.html'


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'materials/article_create.html'
    success_url = reverse_lazy('article_list')  # Перенаправление на список статей после добавления


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'materials/article_detail.html'
