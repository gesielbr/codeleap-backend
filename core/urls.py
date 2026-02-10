from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # O correto é .urls
    path('', include('posts.urls')),
]

