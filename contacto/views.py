from django.shortcuts import render
from django.http import JsonResponse
from contacto.forms import ContactoForm

def registrar_mensaje(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'status':'ok',
                'mensaje':'Registro exitoso'
            })
        else:
            return JsonResponse({
                'status':'error',
                'errors':form.errors
            })
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form':form})