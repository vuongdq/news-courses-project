# Generated by Django 5.1.7 on 2025-03-24 11:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Tên danh mục')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
            ],
            options={
                'verbose_name': 'Danh mục khoá học',
                'verbose_name_plural': 'Danh mục khoá học',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created_at'], 'verbose_name': 'Khoá học', 'verbose_name_plural': 'Khoá học'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='name',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
        migrations.AddField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Ngày tạo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Giá giảm'),
        ),
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Thời lượng (hh:mm:ss)'),
        ),
        migrations.AddField(
            model_name='course',
            name='enrollment_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Số người đăng ký'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Giảng viên'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Nổi bật'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_free',
            field=models.BooleanField(default=False, verbose_name='Miễn phí'),
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Giá'),
        ),
        migrations.AddField(
            model_name='course',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày xuất bản'),
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('draft', 'Bản nháp'), ('published', 'Đã xuất bản')], default='draft', max_length=10, verbose_name='Trạng thái'),
        ),
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='courses/thumbnails/', verbose_name='Ảnh đại diện'),
        ),
        migrations.AddField(
            model_name='course',
            name='title',
            field=models.CharField(default='Khóa học mẫu', max_length=250, verbose_name='Tên khoá học'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Mô tả khoá học'),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.coursecategory', verbose_name='Danh mục'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Tên bài học')),
                ('slug', models.SlugField(blank=True, max_length=250, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Nội dung bài học')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='Link video')),
                ('duration', models.DurationField(blank=True, null=True, verbose_name='Thời lượng (hh:mm:ss)')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Thứ tự')),
                ('is_preview', models.BooleanField(default=False, verbose_name='Xem trước miễn phí')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course', verbose_name='Khoá học')),
            ],
            options={
                'verbose_name': 'Bài học',
                'verbose_name_plural': 'Bài học',
                'ordering': ['order', 'created_at'],
            },
        ),
    ]
