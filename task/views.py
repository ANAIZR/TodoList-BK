from rest_framework.viewsets import ModelViewSet
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework.permissions import BasePermission
from users.utils import validate_token, get_payload_from_token
from rest_framework.response import Response
from users.models import User
from users.serializer import UserSerializer


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
        token_from_client = header.split()[1]
        if not validate_token(token_from_client):
            return Response({"message": "Token no valido"})

        payload = get_payload_from_token(token_from_client)
        print(payload.get("user_id"))
        # vamos a buscar al objeto de la id
        user = UserSerializer(User.objects.get(pk=payload.get("user_id"))).data
        print("is_super_user", user.get("is_super_user"))
        if not user.get("is_super_user"):
            return Response({"message": "No tienes permiso para esta acción"})
        queryset = TaskSerializer(
            Task.objects.filter(user_id=user.get("id")), many=True
        ).data
        return Response(queryset)
