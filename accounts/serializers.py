from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'employee_id']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if len(attrs['employee_id']) < 11 :
            raise serializers.ValidationError({'error':'must be more than 11 characters'})
        return super().validate(attrs)

    def create(self, validated_data):
        User=get_user_model()
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user , username = validated_data['username'],bio="this is my bio")
        return user