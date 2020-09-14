from django.contrib import admin
from django.urls import path, include

from backend_main.api_views import get_router_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hr-api/', include(get_router_urls()))
]
