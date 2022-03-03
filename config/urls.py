from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view, name='docs'),
    path('api/', include("api.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
