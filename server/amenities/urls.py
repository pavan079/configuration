# amenities/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmenityViewSet

router = DefaultRouter()
router.register(r'amenities', AmenityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
