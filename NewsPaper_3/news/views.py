
# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import News
from .forms import NewsForm

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    ordering = ['-pub_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-pub_date')

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news:news_list')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})
