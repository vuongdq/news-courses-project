from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from taggit.managers import TaggableManager  # Sử dụng django-taggit cho Tags

# Model cho Danh mục (Category)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Tên danh mục")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="Slug")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả")

    class Meta:
        verbose_name = "Danh mục"
        verbose_name_plural = "Danh mục"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Model cho Tin tức (News)
class News(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Bản nháp'),
        ('published', 'Đã xuất bản'),
    )

    title = models.CharField(max_length=250, verbose_name="Tiêu đề")
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name="Slug")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Danh mục")
    tags = TaggableManager(verbose_name="Thẻ")  # Quản lý Tags bằng django-taggit
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Tác giả")
    thumbnail = models.ImageField(upload_to='news/thumbnails/', blank=True, null=True, verbose_name="Ảnh đại diện")
    content = models.TextField(verbose_name="Nội dung")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="Ngày xuất bản")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Trạng thái")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Lượt xem")
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")

    class Meta:
        verbose_name = "Tin tức"
        verbose_name_plural = "Tin tức"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Model cho Ảnh bổ sung trong nội dung (NewsImage)
class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images', verbose_name="Tin tức")
    image = models.ImageField(upload_to='news/images/', verbose_name="Ảnh")
    caption = models.CharField(max_length=200, blank=True, null=True, verbose_name="Chú thích")

    class Meta:
        verbose_name = "Ảnh tin tức"
        verbose_name_plural = "Ảnh tin tức"

    def __str__(self):
        return f"Ảnh của {self.news.title}"