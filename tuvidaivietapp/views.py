from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from news.models import News
from courses.models import Course
from .forms import RegisterForm

def home(request):
    featured_news = News.objects.filter(status='published', is_featured=True).order_by('-published_at')[:3]
    featured_courses = Course.objects.filter(status='published', is_featured=True).order_by('-published_at')[:3]
    return render(request, 'home.html', {
        'featured_news': featured_news,
        'featured_courses': featured_courses
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})