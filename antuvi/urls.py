from django.urls import path
from antuvi.views import api, antuvi_index

urlpatterns = [
    path('api/', api),           # Thay url(r'^api') bằng path('api/')
    path('', antuvi_index)  # Thay url(r'^$') bằng path('')
]