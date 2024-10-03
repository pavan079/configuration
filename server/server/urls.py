from django.contrib import admin
from django.urls import path, include  # Adjusted import for including app URLs
from housekeeping import views  # Ensure housekeeping views are correctly imported

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Housekeeping URLs
    path('api/housekeepers/', views.housekeeper_list, name='housekeeper_list'),
    path('api/housekeepers/<int:pk>/', views.housekeeper_delete, name='housekeeper_delete'),

    # Root URL (if this is a home page or similar)
    path('', views.home, name='home'),  
    
    # Amenities app URLs (make sure this path doesn't conflict with others)
    path('api/', include('amenities.urls')),

        path('api/', include('roomlist.urls')),  # Include roomlist URLs

]
