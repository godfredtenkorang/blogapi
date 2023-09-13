from django.urls import path
from users.apis.views import registration_view
from rest_framework.authtoken.views import obtain_auth_token
from users.apis import views

urlpatterns = [
    path('register', registration_view, name='register-view'),
    path('login', obtain_auth_token, name='login-view'),
    path('update_profile', views.update_profile),
    path('profile', views.profile),
]