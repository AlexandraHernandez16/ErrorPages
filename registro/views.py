from django.shortcuts import render
from registro.alumno import alumno
from .forms import ContactoForm

def registrarAlumno(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Los datos ya pasaron las validaciones de front y back
            nombre = form.cleaned_data['nombre']
            matricula = form.cleaned_data['matricula']
            correo = form.cleaned_data['correo']
            telefono = form.cleaned_data['telefono']
            rfc = form.cleaned_data['rfc']
            contraseña = form.cleaned_data['contraseña']
            
            return render(request, 'registro/registro.html', {'form': form, 'success': True})
    else:
        form = ContactoForm()
    
    return render(request, 'registro/registro.html', {'form': form})