from django.urls import path

from .views import (
    ArticleListView,
    ArticleEditView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentCreateView
    )
urlpatterns = [
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:article_pk>/comment/', CommentCreateView.as_view(), name='comment_new'),
    path('', ArticleListView.as_view(), name = 'article_list'),
]