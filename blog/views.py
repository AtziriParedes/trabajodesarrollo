from django.shortcuts import render, redirect
from .models import Post

def publicaciones(request):
    posts = Post.objects.all().order_by('-fecha')
    return render(request, 'blog/publicaciones.html', {'posts': posts})

def crear_post(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        contenido = request.POST.get("contenido", "")
        autor = request.POST.get("autor", "")
        imagen = request.POST.get("imagen", "") # Captura la URL del campo nuevo

        # Campos de macros nutrimentales
        calorias = request.POST.get("calorias", "")
        proteinas = request.POST.get("proteinas", "")
        carbohidratos = request.POST.get("carbohidratos", "")
        azucares = request.POST.get("azucares", "")
        sodio = request.POST.get("sodio", "")
        vitaminas = request.POST.get("vitaminas", "")

        if not titulo:
            return render(request, "blog/crear.html", {"error": "El título no puede estar vacío"})

        # Guardamos todo en la base de datos
        Post.objects.create(
            titulo=titulo,
            contenido=contenido,
            autor=autor,
            imagen=imagen,
            calorias=calorias,
            proteinas=proteinas,
            carbohidratos=carbohidratos,
            azucares=azucares,
            sodio=sodio,
            vitaminas=vitaminas
        )
        return redirect("publicaciones")

    return render(request, 'blog/crear.html')