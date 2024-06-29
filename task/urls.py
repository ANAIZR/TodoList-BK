from .views import CategoryViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#debemos registrar las rutas
router.register(r"categories",CategoryViewSet)
router.register(r"tasks",TaskViewSet)


urlpatterns = router.urls
