from rest_framework import serializers
from users.serializers import UserListSerializer
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserListSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status', 'assigned_users']

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'task_type']

class AssignTaskSerializer(serializers.Serializer):
    task_id = serializers.UUIDField()
    user_ids = serializers.ListField(child=serializers.UUIDField())
