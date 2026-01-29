from rest_framework import serializers
from .models import Profile, LeftBlock


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class LeftBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeftBlock
        fields = "__all__"