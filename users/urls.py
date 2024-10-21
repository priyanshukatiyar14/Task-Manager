from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user_list_create'),
    path('<str:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_retrieve_update_destroy'),
]