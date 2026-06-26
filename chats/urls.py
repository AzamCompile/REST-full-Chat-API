from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, MessageViewSet

router = DefaultRouter()

router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls