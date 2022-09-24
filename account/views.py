from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from account.models import Profile, User
from account.permissions import IsAuthorPermission
from account.serializers import UserProfileSerializer, RegisterSerializer
from shop.models import Category


class SenderRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Profile.objects.create(user=user, is_sender=True)


class BuyerRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Profile.objects.create(user=user, is_sender=False)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        if user:
            Profile.objects.create(user=user, is_sender=False)


class UserProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser, ]
