from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=50, choices=[('manager', 'Manager'), ('developer', 'Developer'), ('tester', 'Tester')], default='developer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name