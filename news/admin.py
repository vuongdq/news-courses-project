from django.contrib import admin
from .models import Category, News, NewsImage

# Đăng ký Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

# Inline cho NewsImage
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1  # Số lượng ảnh mặc định có thể thêm

# Đăng ký News
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_at', 'is_featured')
    list_filter = ('status', 'category', 'is_featured', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    inlines = [NewsImageInline]
    list_editable = ('status', 'is_featured')
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = "Đánh dấu là đã xuất bản"

# Đăng ký NewsImage (tuỳ chọn nếu muốn quản lý riêng)
@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ('news', 'image', 'caption')
    search_fields = ('news__title', 'caption')