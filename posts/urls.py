from django.urls import path
from .views import PostViewSet


post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    
    path('careers/', post_list, name='post-list'),
    
    
    path('careers/<int:pk>/', post_detail, name='post-detail'),
]