from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.core.apps if hasattr(admin.site, 'core') else admin.site.urls),
    path('', include('blog.urls')),
    
    # ESTA LÍNEA ES LA QUE FALTA PARA ARREGLAR EL ERROR:
    path("__reload__/", include("django_browser_reload.urls")),
]