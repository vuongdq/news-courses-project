"""
URL configuration for tuvidaivietapp project.
...
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, register, profile  # Thêm import profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('news/', include('news.urls')),
    path('courses/', include('courses.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),  # Sử dụng hàm profile đã import
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)