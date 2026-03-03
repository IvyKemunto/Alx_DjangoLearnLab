from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserListSerializer


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer for notifications."""
    actor = UserListSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target_post', 'timestamp', 'is_read']
        read_only_fields = ['id', 'actor', 'verb', 'target_post', 'timestamp']
