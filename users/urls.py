from .views import *
from django.urls import path

urlpatterns = [
    path('register/', UserViewSet.as_view({'post': 'create'}),name='user_view'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('updateprofile/', UserProfileUpdateView.as_view(), name='profile-update'),
]
