# Generated by Django 5.1.2 on 2024-10-21 16:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('role', models.CharField(choices=[('manager', 'Manager'), ('developer', 'Developer'), ('tester', 'Tester')], default='developer', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
