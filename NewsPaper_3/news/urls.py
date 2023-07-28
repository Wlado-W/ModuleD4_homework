from django.urls import path
from .views import NewsListView, NewsDetailView, add_news, search_news, edit_news, delete_news

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('add/', add_news, name='add_news'),
    path('search/', search_news, name='search_results'),
    path('<int:pk>/edit/', edit_news, name='edit_news'),
    path('<int:pk>/delete/', delete_news, name='delete_news'),
]

