from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/profile/', UserProfileUpdateView.as_view(), name='profile-update'),
]
