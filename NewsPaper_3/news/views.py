
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import News
from .forms import NewsForm
from django.db.models import Q
from django.core.paginator import Paginator

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    ordering = ['-pub_date']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = self.request.GET.get('count', self.paginate_by)
        paginator = Paginator(context['news_list'], count)
        page = self.request.GET.get('page')
        context['news_list'] = paginator.get_page(page)
        context['count'] = int(count)
        return context

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

def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news:news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'edit_news.html', {'form': form})

def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news:news_list')
    return render(request, 'delete_news.html', {'news': news})
def search_news(request):
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    date = request.GET.get('date', '')

    search_q = Q()
    if title:
        search_q |= Q(title__icontains=title)
    if author:
        search_q |= Q(author__username__icontains=author)
    if date:
        search_q |= Q(pub_date__gt=date)

    news_list = News.objects.filter(search_q)
    return render(request, 'search_news.html', {'news_list': news_list})
