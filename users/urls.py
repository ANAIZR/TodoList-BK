from .views import UserViewSet, AuthenticationView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()

# debemos registrar las rutas
router.register(r"users", UserViewSet)


urlpatterns = [path(r"login", AuthenticationView.as_view(),name='custom_login'), *router.urls]
