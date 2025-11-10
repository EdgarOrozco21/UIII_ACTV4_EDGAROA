from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Agregado para MEDIA
from django.conf.urls.static import static # Agregado para MEDIA

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_clientes.urls')),
    path('', include('app_empleados.urls')),
]

# Configuración para servir archivos MEDIA (imágenes subidas) en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)