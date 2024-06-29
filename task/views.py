from rest_framework.viewsets import ModelViewSet
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework.permissions import BasePermission
from users.utils import validate_token
from rest_framework.response import Response


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Para poder instersectar la funcion que lista todas las tareas usamos list


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        header = request.headers.get("Authorization")
        if not validate_token(header.split()[1]):
            return Response({"message": "Token no valido"})
        queryset = CategorySerializer(Task.objects.all(), many=True).data
        return Response(queryset)
