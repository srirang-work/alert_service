# alert/serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Alert

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'user', 'cryptocurrency', 'target_price', 'status', 'created_at', 'updated_at']
