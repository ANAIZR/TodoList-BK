from .models import User
from .serializer import UserSerializer, UserLoginSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthenticationView(APIView):
    def post(self, request):
        # request.data = la información que recibimos del clinte
        user_request = UserLoginSerializer(data=request.data)
        if not user_request.is_valid():
            return Response({"message": "Email y/o password incorrectos"}, status=401)

        # BUSCAMOS EL USUARIO PORCORREO
        user = User.objects.get(email=user_request.data["email"])

        if not user:
            return Response({"message": "Email y/o password incorrectos"}, status=401)

        user_serializer = UserSerializer(user).data
        if not check_password(
            user_request.data["password"], user_serializer.get("password")
        ):
            return Response({"message": "Email y/o password incorrectos"}, status=401)
        print(user)
        return Response({"message": "Todo bien"})
