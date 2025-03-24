from django.shortcuts import render, get_object_or_404
from .models import Course

def course_list(request):
    course_list = Course.objects.filter(status='published').order_by('-published_at')
    return render(request, 'courses/course_list.html', {'course_list': course_list})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, status='published')
    lessons = course.lessons.all().order_by('order')  # Sửa từ lesson_set thành lessons
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons
    })