from django.shortcuts import render

# Create your views here.
def index(request): 
    print("Alguien entró a la página principal")
    return render(request, 'core/index.html')


def onePage(request):
    return render(request, 'core/onePage.html')


def katia(request):
    return render(request, 'core/katia.html')