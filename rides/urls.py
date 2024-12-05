from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, RideViewSet

router = DefaultRouter()
router.register('rides', RideViewSet, basename='ride')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', obtain_auth_token, name='token'), 
    path('', include(router.urls)),
]