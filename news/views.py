from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news_list = News.objects.filter(status='published').order_by('-published_at')
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status='published')
    news.views_count += 1
    news.save()
    return render(request, 'news/news_detail.html', {'news': news})