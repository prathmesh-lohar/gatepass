from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlagElementViewSet,GatepassViewSet,EntryViewSet,MatchElementViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'gatepasses', GatepassViewSet, basename='gatepass')
router.register(r'class-entries', EntryViewSet)
router.register(r'face_detect_flag', FlagElementViewSet, basename="face_detect_flag")
router.register(r'realtime_match', MatchElementViewSet, basename="realtime_match")

# # Register the viewset with the router
# router.register(r'face_detect_flag', FlagElementViewSet, basename="face_detect_flag")

# Include the router URLs in the main URL configuration
urlpatterns = [
    path('api/', include(router.urls)),
]



