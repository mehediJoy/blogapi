from django.urls import path
from .views import PostList, PostDetail, UserList, UesrDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UesrDetail.as_view()),
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]
