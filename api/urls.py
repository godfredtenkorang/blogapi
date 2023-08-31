from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreatelView
from . import views


urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('<int:pk>/blog/', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/new/', BlogCreatelView.as_view(), name='blog-create'),
    # path('<pk>/blog/', views.blog_detail, name='blog_detail'),
]