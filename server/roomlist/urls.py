from django.urls import path, include
from . import views  # or import your RoomViewSet if using ViewSets

urlpatterns = [
    path('api/rooms/', views.RoomListCreateView.as_view()),  # Update the view name based on your implementation
    # or if you're using a ViewSet with routers
    # path('api/', include(router.urls)),
]
