from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.HomeView.as_view(), name='home'),

    # Authentication
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Posts CRUD
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

    # Search and Tags
    path('search/', views.search_posts, name='search'),
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts-by-tag'),
]
