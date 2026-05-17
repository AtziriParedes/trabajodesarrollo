from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicaciones, name='publicaciones'),
    path('crear/', views.crear_post, name='crear_post'),
]