from django.db import models
from users.models import User
import uuid

class Task(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=100, choices=[('feature', 'Feature'), ('bug', 'Bug')], default='feature')
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending')
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
