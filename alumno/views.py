from django.shortcuts import render
from alumno.alumno import alumno

def pintarAlumno(request):
    a1 = alumno("Katia", "Hernández", 22, "20233TN166")

    #¿Me está llengando info de un form?
    if(request.method == "POST"):
        #Tratar esa info
        nombre = request.POST.get("nombre").upper()
        return render(
        request, 
        "alumno/informacion.html", 
        {
          "seEnvio":True,
          "alumno1": a1,
          "alumno2": alumno(nombre, "León",20, "20233TN 175"),
          "nombre": nombre
        }
    )
       

    ##Render
    return render(
        request, 
        "alumno/informacion.html", 
        {
            "alumno1": a1,
            "alumno2": alumno("Daniel", "León",20, "20233TN175")
        }
    )
