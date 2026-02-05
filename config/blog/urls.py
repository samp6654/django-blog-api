from django.urls import path
from .views import CommentDetailView, CommentListCreateView, PostListCreateView, PostDetailView, LikePostView

urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:pk>/like/', LikePostView.as_view()),

    path("posts/<int:post_id>/comments/", CommentListCreateView.as_view()),
    path("comments/<int:pk>/", CommentDetailView.as_view()),

    
]
