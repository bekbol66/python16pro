from django.urls import path
from .views import TaskViewset

urlpatterns = [
    path('', TaskViewset.as_view({'get': 'list',
                                  'post': 'create'}), name='task_list'),

    path('<int:pk>/', TaskViewset.as_view({'get': 'retrieve', 'put': 'update',
                                           'delete': 'destroy'}), name='task_detail'),
]