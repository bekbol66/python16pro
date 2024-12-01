from .models import Task
from rest_framework import viewsets,permissions
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = ['completed']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
