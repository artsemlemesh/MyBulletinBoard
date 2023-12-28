from django.urls import path
from .views import PostList, PostCreate, PostDetail, CommentCreate, PostUpdate, CategoryListView


app_name = 'board'
urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_add'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_edit'),
    path('comment/', CommentCreate.as_view(), name='comment_add'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list')
]