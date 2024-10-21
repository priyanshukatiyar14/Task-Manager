from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, AssignTaskAPIView, RetrieveUserTasksAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('assign/', AssignTaskAPIView.as_view(), name='assign_task'),
    path('user/<str:user_id>/', RetrieveUserTasksAPIView.as_view(), name='retrieve_user_tasks'),
    path('<str:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_retrieve_update_destroy'),
]