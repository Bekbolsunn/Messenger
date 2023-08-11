from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    profile_url = serializers.HyperlinkedRelatedField(
        view_name='user-profile-detail',
        read_only=True,
        lookup_field='user',
        lookup_url_kwarg='pk'
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_url')