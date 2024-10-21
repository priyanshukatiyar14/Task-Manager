from . models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . serializers import UserSerializer
from tasks.models import Task
from rest_framework.response import Response
from rest_framework import status

class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            user_serialized_data = self.serializer_class(data=request.data)
            if user_serialized_data.is_valid():
                user_serialized_data.save()
                return Response(user_serialized_data.data, status=status.HTTP_201_CREATED)
            return Response(user_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self, request, *args, **kwargs):
        try:
            users = self.get_queryset()
            user_serialized_data = self.serializer_class(users, many=True)
            return Response(user_serialized_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            tasks = Task.objects.filter(assigned_users=user.id)
            user_serialized_data = self.serializer_class(user).data
            user_serialized_data['tasks'] = [task.id for task in tasks]
            return Response(user_serialized_data, status=status.HTTP_200_OK)        
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            user_serialized_data = self.serializer_class(user, data=request.data, partial=True)
            if user_serialized_data.is_valid():
                user_serialized_data.save()
                return Response(user_serialized_data.data, status=status.HTTP_200_OK)
            return Response(user_serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Task.DoesNotExist:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            tasks = Task.objects.filter(assigned_users=user.id)
            for task in tasks:
                task.assigned_users.remove(user.id)
            return self.destroy(request, *args, **kwargs)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

