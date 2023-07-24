from django.urls import path
from .views import NewsListView, NewsDetailView, add_news

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('add', add_news, name='add_news'),
]
