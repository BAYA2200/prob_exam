from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from shop.models import Category, Item
from shop.permissions import CategoryPermission
from shop.serializers import CategorySerializer, ItemSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [CategoryPermission, ]

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Category.objects.create(user=user, is_sender=False)


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [CategoryPermission]


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemCreateAPIView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = [CategoryPermission, ]

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Item.objects.create(user=user, is_sender=False)
