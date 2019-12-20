from django.contrib.auth.models import User, Group
from rest_framework import serializers
from SmartAlertServer.models import Contact

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['url', 'username', 'email', 'groups', 'name', 'dob', 'is_god', 'date_added']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']