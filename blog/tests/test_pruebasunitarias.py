import pytest
from django.urls import reverse
from datetime import datetime
from blog.models import Post

@pytest.mark.django_db
def test_publicaciones_status_code(client):
    url = reverse("publicaciones")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_api_posts_status_code(client):
    url = reverse("api_posts")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_api_json_status_code(client):
    url = reverse("json_api")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_api_post_detail_status_code(client):
    post = Post.objects.create(
        titulo="Avena",
        contenido="Cocinar avena",
        autor="Mariana"
    )
    url = reverse("api_post_detail", args=[post.id])
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()["id"] == post.id

@pytest.mark.django_db
def test_crear_post(client):
    url = reverse("crear_post")
    data = {
        "titulo": "Licuado",
        "contenido": "Mezclar fresas con leche"
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Post.objects.count() == 1

@pytest.mark.django_db
def test_xss_protection(client):
    url = reverse("crear_post")
    payload = "<script>alert('XSS')</script>"
    response = client.post(url, {
        "titulo": "Avena Safe",
        "contenido": payload
    })
    assert response.status_code == 302
    post = Post.objects.first()
    assert "<script>" in post.contenido
    assert "alert('XSS')" in post.contenido

@pytest.mark.django_db
def test_sql_injection_protection(client):
    url = reverse("crear_post")
    payload = "'; DROP TABLE blog_post;"
    response = client.post(url, {
        "titulo": "Intento",
        "contenido": payload
    })
    assert response.status_code == 302
    assert Post.objects.count() == 1

@pytest.mark.django_db
def test_titulo_no_vacio(client):
    url = reverse("crear_post")
    response = client.post(url, {
        "titulo": "",
        "contenido": "Algo de comida"
    })
    assert Post.objects.count() == 0

@pytest.mark.django_db
def test_api_posts_returns_json_list(client):
    Post.objects.create(titulo="Receta1", contenido="Texto", autor="Juan")
    Post.objects.create(titulo="Receta2", contenido="Texto2", autor="Ana")
    
    url = reverse("api_posts")
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert "titulo" in data[0]