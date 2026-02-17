from django.shortcuts import render
from django.http import JsonResponse
from .forms import ErrorReportForm
from .models import ErrorReport

# Create your views here.

def reporte_error_view(request):
    if request.method == 'GET':
        form = ErrorReportForm()
        return render(request, 'error_reports/reporte_error.html', {'form': form})
    
    elif request.method == 'POST':
        form = ErrorReportForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status': 'ok',
                'mensaje': 'registro exitoso'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'mensaje': 'algo salio mal',
                'errors': form.errors
            })


def obtener_reportes_view(request):
    reportes = ErrorReport.objects.all()
    data = []
    for reporte in reportes:
        data.append({
            'id': reporte.id,
            'titulo': reporte.titulo,
            'descripcion': reporte.descripcion,
            'tipo_error': reporte.tipo_error,
            'url': reporte.url,
            'metodo_http': reporte.metodo_http,
            'ip_cliente': reporte.ip_cliente,
            'fecha_reporte': reporte.fecha_reporte.strftime('%Y-%m-%d %H:%M:%S'),
            'activo': reporte.activo
        })
    return JsonResponse(data, safe=False)
