from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import Group
from rest_framework import viewsets
from SmartAlertServer.serializers import UserSerializer, GroupSerializer
from SmartAlertServer.models import Contact


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
