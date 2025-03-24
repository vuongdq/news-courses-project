from django.contrib import admin
from .models import CourseCategory, Course, Lesson

# Đăng ký CourseCategory
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

# Inline cho Lesson
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1  # Số bài học mặc định có thể thêm
    prepopulated_fields = {'slug': ('title',)}

# Đăng ký Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'price', 'is_free', 'is_featured', 'created_at')
    list_filter = ('status', 'category', 'is_free', 'is_featured', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [LessonInline]
    list_editable = ('status', 'is_free', 'is_featured')
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = "Đánh dấu là đã xuất bản"

# Đăng ký Lesson (tuỳ chọn nếu muốn quản lý riêng)
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'is_preview', 'created_at')
    list_filter = ('course', 'is_preview')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}