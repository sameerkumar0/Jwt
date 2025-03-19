from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserProfileView.as_view(), name='users'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
