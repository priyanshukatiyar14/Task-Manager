from . models import Task
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from . serializers import TaskSerializer, TaskCreateSerializer, AssignTaskSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        return TaskSerializer
    
    def get(self, request, *args, **kwargs):
        try:
            tasks = self.get_queryset()
            task_serialized_data = self.serializer_class(tasks, many=True)
            return Response(task_serialized_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request, *args, **kwargs):
        try:
            task_serialized_data = self.get_serializer(data=request.data)
            if task_serialized_data.is_valid():
                task_serialized_data.save()
                return Response(task_serialized_data.data, status=status.HTTP_201_CREATED)
            return Response(task_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class TaskRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        try:
            task = self.get_object()
            task_serialized_data = self.serializer_class(task).data
            return Response(task_serialized_data, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, *args, **kwargs):
        try:
            task = self.get_object()
            task_serialized_data = self.serializer_class(task, data=request.data, partial=True)
            if task_serialized_data.is_valid():
                task_serialized_data.save()
                return Response(task_serialized_data.data, status=status.HTTP_200_OK)
            return Response(task_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, *args, **kwargs):
        try:
            task = self.get_object()
            for user in task.assigned_users.all():
                task.assigned_users.remove(user)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AssignTaskAPIView(CreateAPIView):
    serializer_class = AssignTaskSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            task_id = serializer.validated_data['task_id']
            user_ids = serializer.validated_data['user_ids']
            task = Task.objects.get(id=task_id)
            task.assigned_users.add(*user_ids)
            return Response(status=status.HTTP_201_CREATED)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({'error': e}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RetrieveUserTasksAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(assigned_users=user_id)
        
    
    def get(self, request, *args, **kwargs):
        try:
            tasks = self.get_queryset()
            task_serialized_data = self.serializer_class(tasks, many=True)
            return Response(task_serialized_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)