from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GatepassViewSet,EntryViewSet

router = DefaultRouter()
router.register(r'gatepasses', GatepassViewSet, basename='gatepass')
router.register(r'class-entries', EntryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
