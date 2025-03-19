from django.urls import path
from .views import RegisterView, LoginView, UserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserView.as_view(), name='users'),
    path('users/<int:pk>/', UserView.as_view(), name='UserProfile'),
]
