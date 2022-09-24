from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user_profile', views.UserProfileViewSet, basename='user_profile')

urlpatterns = [
    path('api/account/register/sender/', views.SenderRegisterView.as_view()),
    path('api/account/register/buyer/', views.BuyerRegisterView.as_view()),
]