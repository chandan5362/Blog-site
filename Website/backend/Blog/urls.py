from django.urls import path
from Blog.views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView, BlogPostCategoryView

urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('featured', BlogPostFeaturedView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),]