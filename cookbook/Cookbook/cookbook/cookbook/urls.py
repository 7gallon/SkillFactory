from django.contrib import admin
from django.urls import path, include

from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipes.urls')),
    path('openapi', get_schema_view(
        title='cookbook',
        description="API description"),
        name='openapi-schema'),

]
