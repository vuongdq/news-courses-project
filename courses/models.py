from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Model cho Danh mục Khoá học (CourseCategory)
class CourseCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Tên danh mục")
    slug = models.SlugField(max_length=100, unique=True, blank=True, verbose_name="Slug")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả")

    class Meta:
        verbose_name = "Danh mục khoá học"
        verbose_name_plural = "Danh mục khoá học"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Model cho Khoá học (Course)
class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Bản nháp'),
        ('published', 'Đã xuất bản'),
    )

    title = models.CharField(max_length=250, verbose_name="Tên khoá học")
    slug = models.SlugField(max_length=250, unique=True, blank=True, verbose_name="Slug")
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, verbose_name="Danh mục")
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Giảng viên")
    thumbnail = models.ImageField(upload_to='courses/thumbnails/', blank=True, null=True, verbose_name="Ảnh đại diện")
    description = models.TextField(verbose_name="Mô tả khoá học")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Giá")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Giá giảm")
    duration = models.DurationField(blank=True, null=True, verbose_name="Thời lượng (hh:mm:ss)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="Ngày xuất bản")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Trạng thái")
    enrollment_count = models.PositiveIntegerField(default=0, verbose_name="Số người đăng ký")
    is_free = models.BooleanField(default=False, verbose_name="Miễn phí")
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")

    class Meta:
        verbose_name = "Khoá học"
        verbose_name_plural = "Khoá học"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# Model cho Bài học (Lesson)
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name="Khoá học")
    title = models.CharField(max_length=250, verbose_name="Tên bài học")
    slug = models.SlugField(max_length=250, blank=True, verbose_name="Slug")
    content = models.TextField(verbose_name="Nội dung bài học")
    video_url = models.URLField(blank=True, null=True, verbose_name="Link video")
    duration = models.DurationField(blank=True, null=True, verbose_name="Thời lượng (hh:mm:ss)")
    order = models.PositiveIntegerField(default=0, verbose_name="Thứ tự")
    is_preview = models.BooleanField(default=False, verbose_name="Xem trước miễn phí")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        verbose_name = "Bài học"
        verbose_name_plural = "Bài học"
        ordering = ['order', 'created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.course.title})"