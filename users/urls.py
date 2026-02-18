from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
  path("login", auth_views.LoginView.as_view(), name="login"),
  path('user', views.CreateUserView.as_view(), name="register"),
  
  path('api/user', views.CreateUserAPIView.as_view()),
  path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]