from django.urls import path, include
from api.apis import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blog', views.BlogView)


urlpatterns = [
    path('', include(router.urls))
    # path('blogs/', views.api_blog_view, name='blogs'),
    # path('<pk>/', views.api_detail_blog_view, name='detail'),
    # path('<pk>/update/', views.api_update_blog_view, name='update'),
    # path('<pk>/delete/', views.api_delete_blog_view, name='delete'),
    # path('create', views.api_create_blog_view, name='post'),
]