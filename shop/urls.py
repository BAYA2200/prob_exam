from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('shop', views.CategoryViewSet, basename='shop')
router.register('item', views.ItemViewSet, basename='item')
urlpatterns = [
    path('api/shop/category/', views.CategoryCreateAPIView.as_view()),
    path('api/shop/category/<id>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('api/shop/category/<id>/item', views.ItemCreateAPIView.as_view()),

]