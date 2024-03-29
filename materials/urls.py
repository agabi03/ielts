from django.urls import path
from .views import ArticleListView, ArticleCreateView, ArticleDetailView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/add/', ArticleCreateView.as_view(), name='article_add'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
