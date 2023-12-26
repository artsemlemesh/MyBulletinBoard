from django.urls import path
from .views import PostList, PostCreate

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),


    path('create/', PostCreate.as_view(), name='post_add')
]