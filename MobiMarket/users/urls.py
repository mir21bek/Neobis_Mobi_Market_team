from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import (RegistrationView,
                    LoginView,
                    ProfileUpdateView,
                    CodeSendView,
                    CodeCheckView,
                    LogoutView)

urlpatterns = [
    path('register', RegistrationView.as_view(), name='registration'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', ProfileUpdateView.as_view(), name='profile-update'),
    path('code-send', CodeSendView.as_view(), name='verification-code-send'),
    path('code-check', CodeCheckView.as_view(), name='verification-code-check'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
