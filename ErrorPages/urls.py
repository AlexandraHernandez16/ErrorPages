from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views as core
from alumno import views as alumno
from registro import views as registro
from contacto import views as contacto
from error_reports import views as error_reports

urlpatterns = [
    #Paths con 3 parametros: endpooint, controller, nombre
    path('', core.index, name='index'),
    path('gatos/',core.onePage, name='gatos'),
    path('katia/',core.katia, name='katia'),
    path('alumno/', alumno.pintarAlumno, name='alumno'),
    path('registrar/', registro.registrarAlumno, name='registrarAlumno'),
    path('contacto/', contacto.registrar_mensaje, name = 'contacto'),
    path('reportes-error/', error_reports.reporte_error_view, name='reportes_error'),
    path('obtener-reportes/', error_reports.obtener_reportes_view, name='obtener_reportes'),
    
    # API de Productos (Función)
    path('api/productos/', include('producto_api.urls')),
    
    # API de Productos DRF (Django REST Framework)
    path('', include('producto_drf.urls')),
]

# Esto permite visualizar las imágenes en modo DEBUG (desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
