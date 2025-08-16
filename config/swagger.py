
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Airbnb API Docs",
        default_version='v1',
        description="Документация",
    ),
    public=True,
)